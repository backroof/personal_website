---
layout: page
permalink: /publications/
title: publications
description: Publications by Xihan Ji.
nav: true
nav_order: 2
---

My publications are available in my [ADS library](https://ui.adsabs.harvard.edu/public-libraries/_sqlSKM9Sc2BHwUvwbu8CQ).

{% if site.data.ads_publications.papers.size > 0 %}

## Selected first-author publications

Keywords: JWST, Little Red Dots, Galaxy and black hole evolution, Chemical enrichment

{% for paper in site.data.ads_publications.papers %}
<div class="mb-4">
  <h3><a href="{{ paper.url | escape }}">{{ paper.title | escape }}</a></h3>
  <p>{{ paper.authors | escape }}<br>
  {{ paper.journal | escape }}{% if paper.journal != empty %}, {% endif %}{{ paper.year | escape }} · <strong>{{ paper.citations }} citations</strong> (ADS)</p>
</div>
{% endfor %}

<small>Citation counts updated {{ site.data.ads_publications.updated | escape }}. Counts and ranking may change as ADS is updated.</small>
{% endif %}
