from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^impressum.html$', TemplateView.as_view(template_name='impressum.html'), name='impressum'),
    url(r'^schedule.html$', TemplateView.as_view(template_name='schedule.html'), name='schedule'),
    url(r'^location.html$', TemplateView.as_view(template_name='location.html'), name='location'),
    url(r'^history.html$', TemplateView.as_view(template_name='history.html'), name='history'),
    url(r'^sponsoring.html$', TemplateView.as_view(template_name='sponsoring.html'), name='sponsoring'),
    url(r'^contact.html$', TemplateView.as_view(template_name='contact.html'), name='contact'),

    url(r'robots.txt', TemplateView.as_view(template_name="robots.txt")),

    url(r'^registration.html$', RedirectView.as_view(url='https://www.softwerkskammer.org/activities/socrates-2014'), name='registration'),

    # use gunicorn to serve static files ... might be changed in later releases
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
