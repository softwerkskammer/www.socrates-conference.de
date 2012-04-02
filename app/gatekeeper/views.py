from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext

from registration.models import RegistrationProfile
from registration.forms import RegistrationFormUniqueEmail

from gatekeeper.mail import send_moderation_notices


def register(request, profile_callback=None):
    """
    """
    if request.method == 'POST':
        form = GatekeeperRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(profile_callback=profile_callback)
            return HttpResponseRedirect(reverse('registration_complete'))
    else:
        form = GatekeeperRegistrationForm()
    
    context = RequestContext(request)
    return render_to_response('registration/registration_form.html', { 'form': form }, context_instance=context)


class GatekeeperRegistrationForm(RegistrationFormUniqueEmail):

    def save(self, profile_callback=None):
        """
        """
        new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
                                                                    password=self.cleaned_data['password1'],
                                                                    email=self.cleaned_data['email'],
                                                                    profile_callback=profile_callback,
                                                                    send_email=False)
        send_moderation_notices(new_user)
        return new_user