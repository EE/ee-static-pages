from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .models import StaticPage


@admin.register(StaticPage)
class StaticAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'content')
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('block_indexing', 'title_override', 'meta_description_override'),
        }),
    )
    search_fields = ('name',)
    list_display = ('name', 'slug', 'block_indexing')
    list_filter = ('block_indexing',)
    prepopulated_fields = {"slug": ("name",)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            editor = getattr(settings, 'EE_STATIC_PAGES_EDITOR', 'markdown')
            if editor == 'ckeditor':

                if 'ckeditor' not in settings.INSTALLED_APPS:
                    raise ImproperlyConfigured('Add CKEditor to INSTALLED_APPS')

                from ckeditor.widgets import CKEditorWidget

                kwargs['widget'] = CKEditorWidget(config_name='default')
            else:
                kwargs['help_text'] = mark_safe(
                    _("You can use <a href='http://commonmark.org/help/'>MarkDown</a> formatting")
                )
        return super(StaticAdmin, self).formfield_for_dbfield(db_field, **kwargs)
