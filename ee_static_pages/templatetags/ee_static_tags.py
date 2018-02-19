from django.conf import settings
from django.utils.safestring import mark_safe

from django_markwhat.templatetags.markup import commonmark
from ee_seo_mixin.templatetags.seo_tags import (  # noqa
    register,
    override_title,
    override_description,
    block_indexing
)


@register.filter(is_safe=True)
def render_html(value):
    if getattr(settings, 'EE_STATIC_PAGES_USE_CKEDITOR', False):
        return mark_safe(value)
    else:
        return commonmark(value)
