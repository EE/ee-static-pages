from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ee_seo_mixin.models import SearchEngineOptimizableEntity


class StaticPage(SearchEngineOptimizableEntity):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120)
    slug = models.SlugField(
        max_length=140,
        unique=True,
        null=True,
        blank=True,
        help_text=_('"Slug" is a part of an url adress. \
                    If you leave it blank, it will be generated \
                    automatically from the page\'s name.'))
    content = models.TextField(
        verbose_name=_("Content"))

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while StaticPage.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(StaticPage, self).save(*args, **kwargs)
