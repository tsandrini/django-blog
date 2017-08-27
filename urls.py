from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<page>[a-z][-a-z0-9]+)/$', views.page),
]
