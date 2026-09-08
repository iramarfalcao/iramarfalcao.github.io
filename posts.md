---
layout: default
title: Artigos
description: Artigos e notas de Iramar Falcão.
permalink: /posts/
---

# Artigos

Notas sobre software, projetos, ferramentas e aprendizados do trabalho.

<div class="post-list">
  {% for post in site.posts %}
    <article>
      <p class="meta">{{ post.date | date: "%B %-d, %Y" }}</p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </article>
  {% else %}
    <p>Ainda não há artigos.</p>
  {% endfor %}
</div>
