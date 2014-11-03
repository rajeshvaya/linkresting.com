# dev envrionment settings
from defaults import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'linkresting',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

BASE_URL = "http://localhost:8000/"

SOCIAL_AUTH_TWITTER_KEY = "3T64PQ3FJ26j5TqKUGmRNll9q"
SOCIAL_AUTH_TWITTER_SECRET = "xDACrOjN0YcPUY9XTzglSkojU8VfMUFyCG5lIJAkQrwx0kv361"

SOCIAL_AUTH_FACEBOOK_KEY = "549338855202354"
SOCIAL_AUTH_FACEBOOK_SECRET = "b50a1613042c867f657cf28742a5fe70"
