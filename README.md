# ee-static-pages
Django app for static pages functionality

## installation

1. Install the app through pip:

  ```
  pip install -e git+git@github.com:EE/ee-static-pages.git#egg=ee-static-pages
  ```

2. Add `ee_static_pages` to your installed apps

  ```python
  INSTALLED_APPS = [
      ...
      'ee_static_pages',
      ...
  ]
  ```

## static page object

A static page has 3 simple fields: `name`, `slug` and `content`. On top of that, it also has three SEO related fields (for details, see [ee-seo-mixin](https://github.com/EE/ee-seo-mixin/) package).

## usage

1. In your `urls.py` include urls from ee_static_pages under any path you like:

  ```python
  # urls.py
  from django.conf.urls import url, include
  from ee_static_pages import urls as static_pages

  urlpatterns = [
      ...
      url(r'^pages/', include(static_pages)),
      ...
  ]
  ```

2. In your templates create a `static_page.html`:

  ```python
  # static_page.html
  {% extends 'base.html' %}
  {% load seo_tags %}

  {% block title %}
    {% override_title object default="My title" %}
  {% endblock %}

  {% block  content %}
    {{ object.content }}
  {% endblock content %}

  ```

3. If you need your static page template to have a name other then the default `static_page.html`, you can set `EE_STATIC_PAGES_TEMPLATE_NAME` setting in your `settings.py`.
