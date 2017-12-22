from django.views.generic.detail import DetailView

from .models import StaticPage


class StaticPageView(DetailView):
    model = StaticPage
    template_name = 'static_page.html'
    context_object_name = "seo_object"

    def get_object(self):
        return StaticPage.objects.filter(slug=self.kwargs['slug'])[0]
