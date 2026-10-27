---
layout: default
lang: pt-BR
alt: /projects/
title: Projetos
description: Aplicativos e projetos de Iramar Falcão, fundador da Falcao SL.
permalink: /pt/projects/
---

# Projetos

Aplicativos próprios, do conceito à publicação. Conheça os produtos no [portfólio da Falcao SL](https://falcaosl.com).

## Em destaque

{% include product-cards.html kind="featured" l="pt" %}

## Em desenvolvimento

{% include product-cards.html kind="studio" l="pt" %}

> [!TIP]
> **Participe dos Testes Abertos**: Vários dos nossos aplicativos já possuem versões preliminares ativas no Apple TestFlight e Google Play. Acesse a página do [Programa de Testadores Beta](/pt/testers/) para começar a testar agora mesmo.

## Infraestrutura e serviços

{% for p in site.data.products.infra %}- **{% if p.github %}[{{ p.name }}]({{ p.github }}){% else %}{{ p.name }}{% endif %}**: {{ p.text.pt }}
{% endfor %}
