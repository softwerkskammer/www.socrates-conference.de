from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    url(r'^$', redirect_to, {'url': '/wiki/', 'permanent': False}),
    url(r'', include('social_auth.urls')),

    url(r'^wiki/', include('wakawaka.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
