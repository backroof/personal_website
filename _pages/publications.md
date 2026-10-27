---
layout: page
permalink: /publications/
title: publications
description: Publications by Xihan Ji.
nav: true
nav_order: 2
---

My publications are available in my [ADS library](https://ui.adsabs.harvard.edu/public-libraries/_sqlSKM9Sc2BHwUvwbu8CQ){% if site.data.ads_publications.total_papers %} ({{ site.data.ads_publications.total_papers }} papers, {{ site.data.ads_publications.total_citations }} citations){% endif %}.

## Research highlights:

### 1) Little Red Dots

"Little Red Dots" (LRDs) are a new and puzzling astrophysical phenomenon discovered by JWST. They manifest as an abundant population of optically red and compact galaxies with strong broad Balmer lines, and share similar but not identical spectral features with both stars and accreting black holes. With JWST observations, we discovered that LRDs can be explained by gas-enshrouded accreting black holes ([paper1](https://ui.adsabs.harvard.edu/abs/2025MNRAS.544.3900J/abstract)).

<figure style="margin: 1.5rem auto 2.5rem; max-width: 850px;">
  <a href="{{ '/assets/img/research/lrd-gas-enshrouded-bh.png' | relative_url }}">
    <img src="{{ '/assets/img/research/lrd-gas-enshrouded-bh.png' | relative_url }}" alt="JWST spectrum of Abell 2744-QSO1 and a gas-enshrouded accreting black hole model reproducing its Balmer break." width="1383" height="735" loading="lazy" style="display: block; width: 100%; height: auto; background: white;">
  </a>
  <figcaption style="margin-top: 0.75rem; font-size: 0.875rem; opacity: 0.8;">Continuum modelling of a black-hole-dominated LRD at z = 7.04. Top panel of Figure 6 in paper1.</figcaption>
</figure>

Interestingly, the obscuring gas does not form a simple spherical shell: the strong Lyα emission in the rest-FUV reveals that we need "holes" or a clumpy medium surrounding the accreting black hole. So, holes over a black hole ([paper2](https://ui.adsabs.harvard.edu/abs/2026arXiv260403370J/abstract))!

<figure style="margin: 1.5rem auto 2.5rem; max-width: 560px;">
  <a href="{{ '/assets/img/research/lrd-lya-holes.png' | relative_url }}">
    <img src="{{ '/assets/img/research/lrd-lya-holes.png' | relative_url }}" alt="Broad Lyα emission compared with the narrower Hα profile in a black-hole-dominated LRD, with the best-fit model and residuals." width="756" height="651" loading="lazy" style="display: block; width: 100%; height: auto; background: white;">
  </a>
  <figcaption style="margin-top: 0.75rem; font-size: 0.875rem; opacity: 0.8;">The Lyα profile probes the geometry of the surrounding gas. Top panel of Figure 7 in paper2.</figcaption>
</figure>

Until recently, LRDs were believed to be a predominantly high-redshift phenomenon at z &gt; 4. However, with wide-area surveys including SDSS and DESI, we discovered local, bona fide LRDs at z &lt; 1. The local LRDs, or "LoRDs", allow ground-based follow-up observations due to their proximity, revealing unprecedented spectral details and tracing complex metal absorption and emission from LRDs' gas envelopes ([paper3](https://ui.adsabs.harvard.edu/abs/2026MNRAS.545f2235J/abstract)).

<figure style="margin: 1.5rem auto 2.5rem; max-width: 650px;">
  <a href="{{ '/assets/img/research/lord-optical-spectrum.png' | relative_url }}">
    <img src="{{ '/assets/img/research/lord-optical-spectrum.png' | relative_url }}" alt="Optical spectrum of local LRD J1025+1402, showing annotated Fe II emission and metal absorption features." width="750" height="531" loading="lazy" style="display: block; width: 100%; height: auto; background: white;">
  </a>
  <figcaption style="margin-top: 0.75rem; font-size: 0.875rem; opacity: 0.8;">Metal emission and absorption in the local LRD J1025+1402. Bottom-left panel of Figure 3 in paper3.</figcaption>
</figure>

### 2) Chemical anomalies of early galaxies

In observations, elemental abundances are precise "clocks" that record the progress of stellar evolution and galaxy evolution. In particular, CNO elements are well-calibrated clocks in local galaxies: when C and N are enriched, O is typically much more enriched. However, JWST has revealed a non-negligible fraction of galaxies with enhanced nitrogen in the early Universe, which show super-solar nitrogen abundances yet sub-solar oxygen abundances ([paper4](https://ui.adsabs.harvard.edu/abs/2024MNRAS.535..881J/abstract)).

<figure style="margin: 1.5rem auto 2.5rem; max-width: 850px;">
  <a href="{{ '/assets/img/research/chemical-anomalies-no-oh.png' | relative_url }}">
    <img src="{{ '/assets/img/research/chemical-anomalies-no-oh.png' | relative_url }}" alt="Nitrogen-to-oxygen ratio versus oxygen abundance for local and high-redshift galaxies, highlighting nitrogen enrichment in GS 3073." width="1485" height="795" loading="lazy" style="display: block; width: 100%; height: auto; background: white;">
  </a>
  <figcaption style="margin-top: 0.75rem; font-size: 0.875rem; opacity: 0.8;">Nitrogen enrichment in early galaxies compared with local systems. Figure 4 in paper4.</figcaption>
</figure>

We found that the enrichment patterns of these chemically anomalous galaxies are similar to stars at z = 0! These are stars in globular clusters: extremely dense and old relics of early star formation. Therefore, high-redshift chemically anomalous galaxies might trace a missing progenitor phase of globular cluster formation in observations ([paper5](https://ui.adsabs.harvard.edu/abs/2026MNRAS.545f2110J/abstract)).

<figure style="margin: 1.5rem auto 2.5rem; max-width: 850px;">
  <a href="{{ '/assets/img/research/chemical-anomalies-globular-clusters.png' | relative_url }}">
    <img src="{{ '/assets/img/research/chemical-anomalies-globular-clusters.png' | relative_url }}" alt="Abundance patterns of nitrogen-enhanced galaxies compared with first- and second-generation globular-cluster stars." width="1470" height="732" loading="lazy" style="display: block; width: 100%; height: auto; background: white;">
  </a>
  <figcaption style="margin-top: 0.75rem; font-size: 0.875rem; opacity: 0.8;">Chemical similarities between nitrogen-enhanced galaxies and globular-cluster stars. Bottom panels of Figure 2 in paper5.</figcaption>
</figure>

---

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
