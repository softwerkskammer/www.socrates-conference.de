from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from gatekeeper.forms import GatekeeperRegistrationForm
from gatekeeper.mail import send_approval_notice
from gatekeeper.create_user import create_user


def register(request):
    """
    """
    if request.method == 'POST':
        form = GatekeeperRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = create_user(form.cleaned_data)
            return HttpResponseRedirect(reverse('registration_complete'))
    else:
        form = GatekeeperRegistrationForm()
    
    context = RequestContext(request)
    return render_to_response('registration/registration_form.html', { 'form': form }, context_instance=context)


@login_required
def public_profile(request, user_id):
    usr = get_object_or_404(User, pk=user_id)
    return render_to_response('registration/public_profile.html', 
                            { 'usr': usr, 'profile': usr.get_profile() }, 
                            context_instance=RequestContext(request))


@login_required
def current_user_profile(request):
    return render_to_response('registration/current_user_profile.html', 
                            { 'profile': request.user.get_profile() }, 
                            context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.groups.filter(name=settings.GATEKEEPER_MODERATOR_GROUP).count() > 0)
def pending_registrations(request):
    pending_users = User.objects.filter(is_active=False)
    context = RequestContext(request)
    return render_to_response('registration/pending_registrations.html', 
            { 'pending_registrations': pending_users }, 
            context_instance=context
        )


@login_required
@user_passes_test(lambda u: u.groups.filter(name=settings.GATEKEEPER_MODERATOR_GROUP).count() > 0)
def approve_pending_registrations(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = True
    user.save()
    
    send_approval_notice(user)
    messages.info(request, u'User "%s" has been approved' % user.get_full_name())
    
    return HttpResponseRedirect(reverse('pending_registrations'))


@login_required
@user_passes_test(lambda u: u.groups.filter(name=settings.GATEKEEPER_MODERATOR_GROUP).count() > 0)
def delete_pending_registrations(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.info(request, u'User "%s" has been deleted' % user.email)
    return HttpResponseRedirect(reverse('pending_registrations'))


