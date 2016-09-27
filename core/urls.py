from django.conf.urls import url, include
from core.views import home, thanks, email_teste, email_confim, deposito, profile, module, course, classes, answer_submit
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^email/(?P<code>\w+)/$', email_teste, name='core_email'),
    url(r'^confirmation/(?P<code>\w+)/$', email_confim, name='core_confirmation'),
    url(r'^thanks/$', thanks, name='core_thanks'),
    url(r'^deposito/$', deposito, name='url_core_deposito_conta'),
    url(r'^accounts/signup/', TemplateView.as_view(template_name='core/inscreva-se.html'), name='profile'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', profile, name='profile'),

    url(r'^courses/(?P<course_id>\d+)/$', course, name='url_core_course'),
    url(r'^modules/(?P<module_id>\d+)/$', module, name='url_core_modules'),
    url(r'^class/(?P<class_id>\d+)/$', classes, name='url_core_class'),
    url(r'^answer-submit/(?P<enr_id>\d+)/$', answer_submit, name='url_core_submit_answer'),
]

if settings.DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))
