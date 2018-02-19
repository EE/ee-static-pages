from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ee_seo_mixin.models import SearchEngineOptimizableEntity


class StaticPage(SearchEngineOptimizableEntity):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120)
    slug = models.SlugField(
        max_length=140,
        unique=True,
        help_text=_('"Slug" is a part of an url adress.'))
    content = models.TextField(
        verbose_name=_("Content"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('static-page', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super(StaticPage, self).save(*args, **kwargs)
