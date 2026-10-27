#!/usr/bin/env python3
"""Fetch the five most-cited first-author papers from Xihan Ji's ADS library."""

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

API = "https://api.adsabs.harvard.edu/v1/"
LIBRARY = "_sqlSKM9Sc2BHwUvwbu8CQ"
OUTPUT = Path(__file__).resolve().parents[1] / "_data/ads_publications.json"


def get_json(endpoint, token, **params):
    request = Request(
        API + endpoint + "?" + urlencode(params),
        headers={"Authorization": "Bearer " + token, "Accept": "application/json"},
    )
    for attempt in range(3):
        try:
            with urlopen(request, timeout=60) as response:
                return json.load(response)
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError(f"ADS returned HTTP {exc.code}; check token and library access.") from None
        except (URLError, TimeoutError):
            if attempt == 2:
                raise RuntimeError("ADS could not be reached after three attempts.") from None
        time.sleep(2 ** (attempt + 1))


def is_first_author(author):
    surname, separator, given = author.casefold().partition(",")
    return bool(separator) and surname.strip() == "ji" and given.strip().rstrip(".") in {"xihan", "x"}


def select_papers(documents):
    unique = {doc["bibcode"]: doc for doc in documents}
    papers = []
    for doc in unique.values():
        authors = doc.get("author", [])
        if not authors or not is_first_author(authors[0]):
            continue
        papers.append({
            "bibcode": doc["bibcode"],
            "title": doc["title"][0],
            "authors": "; ".join(authors[:3]) + ("; et al." if len(authors) > 3 else ""),
            "journal": doc.get("pub", ""),
            "year": str(doc.get("year", "")),
            "citations": int(doc.get("citation_count", 0)),
            "url": "https://ui.adsabs.harvard.edu/abs/" + quote(doc["bibcode"], safe="") + "/abstract",
        })
    return sorted(papers, key=lambda p: (-p["citations"], -int(p["year"] or 0), p["bibcode"]))[:5]


def main():
    token = os.environ.get("ADS_API_TOKEN", "").strip()
    if not token:
        raise RuntimeError("Add the ADS_API_TOKEN repository Actions secret before deploying.")
    library = get_json("biblib/libraries/" + LIBRARY, token, raw="true", rows=2000)
    bibcodes = library.get("documents", [])
    if not bibcodes or not all(isinstance(bibcode, str) for bibcode in bibcodes):
        raise RuntimeError("ADS library did not return a nonempty list of bibcodes.")
    total = library.get("metadata", {}).get("num_documents", len(bibcodes))
    if int(total) > len(bibcodes):
        raise RuntimeError("ADS library results were truncated; increase library pagination support.")
    documents = []
    for offset in range(0, len(bibcodes), 50):
        batch = bibcodes[offset:offset + 50]
        query = " OR ".join("bibcode:" + json.dumps(code) for code in batch)
        result = get_json("search/query", token, q=query,
                          fl="bibcode,title,author,pub,year,citation_count", rows=2000)
        response = result["response"]
        if response["numFound"] > len(response["docs"]):
            raise RuntimeError("ADS search results were truncated.")
        documents.extend(response["docs"])
    papers = select_papers(documents)
    if not papers:
        raise RuntimeError("No first-author papers for Xihan Ji were found in the ADS library.")
    unique_documents = {doc["bibcode"]: doc for doc in documents}
    data = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "papers": papers,
        "total_papers": len(unique_documents),
        "total_citations": sum(int(doc.get("citation_count", 0)) for doc in unique_documents.values()),
    }
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {len(papers)} first-author publications from {len(bibcodes)} library records.")
    for paper in papers:
        print(f"{paper['citations']} citations: {paper['title']}")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, KeyError, ValueError, TypeError) as exc:
        print(f"ADS update failed: {exc}", file=sys.stderr)
        sys.exit(1)
