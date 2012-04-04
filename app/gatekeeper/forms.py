from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from gatekeeper.mail import send_moderation_notices
from gatekeeper.models import UserProfile


attrs_dict = { 'class': 'required' }

class GatekeeperRegistrationForm(forms.Form):
    """
    """
    first_name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=_(u'firstname'))
    last_name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=_(u'lastname'))
    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_(u'username'))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)),
                             label=_(u'email address'))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'password (again)'))
    location = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), 
                                label=_(u'location in germany'))
    profession = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), 
                                label=_(u'profession'))
    focus = forms.CharField(required=False, label=_(u'focus'))
    blog_url = forms.URLField(required=False, label=_(u'blog url'))
    twitter_name = forms.CharField(required=False, label=_(u'twitter account'))
    
    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_(u'This username is already taken. Please choose another.'))

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_(u'This email address is already in use. Please supply a different email address.'))
        return self.cleaned_data['email']
        
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data

    def save(self, profile_callback=None):
        """
        """
        new_user = User.objects.create_user(self.cleaned_data['username'], 
                                            self.cleaned_data['email'], 
                                            self.cleaned_data['password1'])
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.is_active = False
        new_user.save()

        user_profile = new_user.get_profile()
        user_profile.focus = self.cleaned_data['focus']
        user_profile.blog_url = self.cleaned_data['blog_url']
        user_profile.twitter_name = self.cleaned_data['twitter_name']
        user_profile.location = self.cleaned_data['location']
        user_profile.profession = self.cleaned_data['profession']
        user_profile.save()
        
        send_moderation_notices(new_user)
        return new_user