from django.contrib import admin
from .models import StaticPage


@admin.register(StaticPage)
class StaticAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'content', 'block_indexing', 'title_override', 'meta_description_override')
