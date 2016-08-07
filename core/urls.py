from django.conf.urls import url, include
from core.views import home, thanks


urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^thanks/$', thanks, name='core_thanks'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', home, name='profile'),

]
