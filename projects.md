---
layout: default
lang: pt-BR
alt: /en/projects/
title: Projetos
description: Aplicativos e projetos de Iramar Falcão, fundador da Falcao SL.
permalink: /projects/
---

# Projetos

Aplicativos próprios, do conceito à publicação. Conheça os produtos no [portfólio da Falcao SL](https://falcaosl.com).

## Em destaque

{% include product-cards.html kind="featured" l="pt" %}

## Em desenvolvimento

{% include product-cards.html kind="studio" l="pt" %}

## Infraestrutura e serviços

{% for p in site.data.products.infra %}- **{% if p.github %}[{{ p.name }}]({{ p.github }}){% else %}{{ p.name }}{% endif %}**: {{ p.text.pt }}
{% endfor %}

