from django.contrib.auth.models import User

from gatekeeper.mail import send_moderation_notices


def create_user(userdata):
    """
    """
    new_user = User.objects.create_user(userdata['username'], 
                                        userdata['email'], 
                                        userdata['password1'])
    new_user.first_name = userdata['first_name']
    new_user.last_name = userdata['last_name']
    new_user.is_active = False
    new_user.save()

    user_profile = new_user.get_profile()
    user_profile.focus = userdata['focus']
    user_profile.blog_url = userdata['blog_url']
    user_profile.twitter_name = userdata['twitter_name']
    user_profile.location = userdata['location']
    user_profile.profession = userdata['profession']
    user_profile.save()
    
    send_moderation_notices(new_user)
    return new_user