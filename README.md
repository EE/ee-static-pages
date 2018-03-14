# ee-static-pages
Django app for static pages functionality with builtin support for [Markdown](http://commonmark.org/) and optional support for [CKEditor](https://github.com/django-ckeditor/django-ckeditor).

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

3. Run `python manage.py migrate ee_static_pages` to create appropriate db tables.

## static page object

A static page has 3 simple fields: `name`, `slug` and `content`. On top of that, it also has three SEO related fields (for details, see [ee-seo-mixin](https://github.com/EE/ee-seo-mixin/) package). The `content` field supports usage of [markdown](http://commonmark.org/) tags out of the box. If you need bigger guns you can switch on CKEditor support (see below).

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

2. In your templates create a `static_page.html`. You can load `seo_tags` and use all the filters from the _ee_seo_mixin_ package. To render content use `rendered_content` method of a `StaticPage` object (it handles different editor backends for you):

  ```python
  # static_page.html
  {% extends 'base.html' %}
  {% load seo_tags %}

  {% block title %}
    {% override_title object default=object.name %}
  {% endblock %}
  
  {% block extrahead %}
    {% override_description my_page default='' %}
    {% block_indexing my_page default=False %}
  {% endblock %}
  
  {% block  content %}
    {{ object.rendered_content }}
  {% endblock content %}
  ```

### CKEditor integration

For this to work you need to have _django-ckeditor_ app installed as per [official repository instructions](https://github.com/django-ckeditor/django-ckeditor#installation). On top of that the only thing you need to do is to set `EE_STATIC_PAGES_EDITOR` setting to `ckeditor` in your `settings.py` file.

### Custom settings

1. If you need your static page template to have a name other then the default `static_page.html`, you can set `EE_STATIC_PAGES_TEMPLATE_NAME` setting in your `settings.py` with an appropriate name.

2. If you want `content` field to be a CKEditor's RichTextField (see above) set `EE_STATIC_PAGES_EDITOR` to `ckeditor` (default is `markdown`)
