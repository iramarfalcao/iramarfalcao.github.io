---
layout: default
title: Posts
description: Posts and notes by Iramar Falcao.
permalink: /posts/
---

# Posts

Notes about software, projects, tools, and the lessons behind the work.

<div class="post-list">
  {% for post in site.posts %}
    <article>
      <p class="meta">{{ post.date | date: "%B %-d, %Y" }}</p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </article>
  {% else %}
    <p>No posts yet.</p>
  {% endfor %}
</div>
