from django.conf.urls import url

from .views import StaticPageView


urlpatterns = [
    url(r'^(?P<slug>[-\w\d]+)/$', StaticPageView.as_view(), name="static-page"),
]
