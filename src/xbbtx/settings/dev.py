from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


#
# Django Debug toolbar
#
INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
