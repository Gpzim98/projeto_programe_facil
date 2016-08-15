from django.conf.urls import url, include
from core.views import home, thanks, email_teste, email_confim


urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^email/(?P<code>\w+)/$', email_teste, name='core_email'),
    url(r'^confirmation/(?P<code>\w+)/$', email_confim, name='core_confirmation'),
    url(r'^thanks/$', thanks, name='core_thanks'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', home, name='profile'),

]
