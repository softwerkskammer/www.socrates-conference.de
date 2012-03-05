from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'', include('social_auth.urls')),

    url(r'^wiki/', include('wakawaka.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
)
