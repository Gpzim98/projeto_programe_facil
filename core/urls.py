from django.conf.urls import url
from core.views import home

urlpatterns = [
    url(r'^$', home),
]
