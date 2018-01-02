# ee-static-pages
Django app for static pages functionality

## installation

1. Install the app through pip:

  ```
  pip install -e git+git@github.com:tadeoos/ee-static-pages.git#egg=ee-static-pages
  ```

2. Add `ee_static_pages` to your installed apps

  ```python
  INSTALLED_APPS = [
      ...
      'ee_static_pages',
      ...
  ]
  ```

3. Make sure you have `APP_DIRS` set to `True` in your `TEMPLATES` setting. If you feel lost, consult the  [docs](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-TEMPLATES-APP_DIRS).

## prerequisites

**Since `ee_static_pages` is dependant upon [`ee-seo-mixin`](https://github.com/EE/ee-seo-mixin), in your project you need a `base.html` template which contains three blocks (see an [example](https://github.com/EE/generator-ee/blob/develop/generators/django/templates/src/templates/base.html)):**

- {% block title %}
- {% block meta_description %}
- {% block extrahead %}


## static page object

A static page has 3 simple fields: `name`, `slug` and `content`. On top of that, it also has three SEO related fields (for details, see `ee-seo-mixin` package mentioned in the above section).

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

2. In your templates create a `static_page.html` file that extends `static_page_base.html`:

  ```python
  # static_page.html
  {% extends 'static_page_base.html' %}

  {% block content %}

  {{ seo_object.content }}

  {% endblock content %}

  ```

  Due to the dependency upon the `ee_seo_mixin` package, you must refer to the page as `seo_object`.
