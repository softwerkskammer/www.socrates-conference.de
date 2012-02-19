from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),
    
    url(r'^wiki/', include('wakawaka.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
