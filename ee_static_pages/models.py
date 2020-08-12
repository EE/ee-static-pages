from django.urls import reverse
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from django_markwhat.templatetags.markup import commonmark
from ee_seo_mixin.models import SearchEngineOptimizableEntity


class StaticPage(SearchEngineOptimizableEntity):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120)
    slug = models.SlugField(
        max_length=140,
        unique=True,
        help_text=_('The unique identifier used in the page\'s URL'))
    content = models.TextField(
        verbose_name=_("Content"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('static-page', kwargs={'slug': self.slug})

    def rendered_content(self):
        editor = getattr(settings, 'EE_STATIC_PAGES_EDITOR', 'markdown')
        if editor == 'ckeditor':
            return mark_safe(self.content)
        else:
            return commonmark(self.content)

    class Meta:
        verbose_name = _("Static Page")
        verbose_name_plural = _("Static Pages")
