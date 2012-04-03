from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to, direct_to_template
from django.views.generic.base import TemplateView

from registration.views import register
from registration.forms import RegistrationFormUniqueEmail

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'', include('social_auth.urls')),

    url(r'^wiki/', include('wakawaka.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/', include('gatekeeper.urls')),

    url(r'robots.txt', direct_to_template, {"template": "robots.txt"}),
)
