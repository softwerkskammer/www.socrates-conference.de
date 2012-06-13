from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from gatekeeper.views import register
from gatekeeper.views import pending_registrations
from gatekeeper.views import approve_pending_registrations
from gatekeeper.views import delete_pending_registrations
from gatekeeper.views import current_user_profile
from gatekeeper.views import edit_current_user_profile
from gatekeeper.views import public_profile
from gatekeeper.forms import LoginForm

urlpatterns = patterns('',
    url(r'^profile/$', current_user_profile, name='current_user_profile'),
    url(r'^profile/edit$', edit_current_user_profile, name='edit_current_user_profile'),
    url(r'^profile/(?P<username>\w+)$', public_profile, name='public_profile'),
    url(r'^register/$', register, name='registration_register'),

    url(r'^register/complete/$',
       direct_to_template,
       {'template': 'gatekeeper/registration_complete.html'},
       name='registration_complete'),

    url(r'^registrations/pending/$', 
        pending_registrations, 
        name='pending_registrations'),
    
    url(r'^registrations/pending/approve/(?P<user_id>\d+)$', 
        approve_pending_registrations, 
        name='approve_pending_registration'),

    url(r'^registrations/pending/delete/(?P<user_id>\d+)$', 
        delete_pending_registrations, 
        name='delete_pending_registration'),

    url(r'^login/$', 
        auth_views.login, 
        {'template_name': 'gatekeeper/login.html', 'authentication_form': LoginForm}, 
        name='auth_login'),

    url(r'^logout/$', 
        auth_views.logout, 
        {'template_name': 'gatekeeper/logout.html'}, 
        name='auth_logout'),

    url(r'^password/change/$', 
        auth_views.password_change, 
        {'template_name':'gatekeeper/password_change_form.html'}, 
        name='auth_password_change'), 

    url(r'^password/change/done/$', 
        auth_views.password_change_done, 
        {'template_name':'gatekeeper/password_change_done.html'}, 
        name='auth_password_change_done'), 

    url(r'^password/reset/$', 
        auth_views.password_reset, 
        {'template_name':'gatekeeper/password_reset.html'}, 
        name='auth_password_reset'),

    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        auth_views.password_reset_confirm,  
        {'template_name':'gatekeeper/password_reset_confirm.html'},
        name='auth_password_reset_confirm'),

    url(r'^password/reset/complete/$', 
        auth_views.password_reset_complete, 
        {'template_name':'gatekeeper/password_reset_complete.html'}, 
        name='auth_password_reset_complete'),

    url(r'^password/reset/done/$', 
        auth_views.password_reset_done, 
        {'template_name':'gatekeeper/password_reset_done.html'}, 
        name='auth_password_reset_done'),
)