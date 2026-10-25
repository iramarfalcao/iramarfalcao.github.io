---
layout: default
lang: en
alt: /projects/
title: Projects
description: Apps and projects by Iramar Falcão, founder of Falcao SL.
permalink: /en/projects/
---

# Projects

Own apps, from concept to release. See the products on the [Falcao SL portfolio](https://falcaosl.com).

## Featured

{% include product-cards.html kind="featured" l="en" %}

## In development

{% include product-cards.html kind="studio" l="en" %}

## Infrastructure and services

{% for p in site.data.products.infra %}- **{% if p.github %}[{{ p.name }}]({{ p.github }}){% else %}{{ p.name }}{% endif %}**: {{ p.text.en }}
{% endfor %}

