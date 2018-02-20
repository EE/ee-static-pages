from django.conf import settings
from django.views.generic.detail import DetailView

from .models import StaticPage


class StaticPageView(DetailView):
    model = StaticPage
    template_name = getattr(settings, 'EE_STATIC_PAGES_TEMPLATE_NAME', 'static_page.html')
