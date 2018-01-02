from django.contrib import admin
from .models import StaticPage


@admin.register(StaticPage)
class StaticAdmin(admin.ModelAdmin):
    pass
