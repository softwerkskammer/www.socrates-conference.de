AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL          = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/accounts/register/complete/'
