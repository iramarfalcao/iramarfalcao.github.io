---
layout: default
lang: pt-BR
alt: /en/posts/
title: Artigos
description: Artigos e notas de Iramar Falcão sobre software, projetos e ferramentas.
permalink: /posts/
---

# Artigos

Notas sobre software, projetos, ferramentas e aprendizados do trabalho.

<div class="post-list">
  {% for post in site.posts %}
    <article>
      <p class="meta">{{ post.date | date: "%d/%m/%Y" }}{% if post.lang == "en" %} · English{% endif %}</p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </article>
  {% else %}
    <p>Ainda não há artigos.</p>
  {% endfor %}
</div>
