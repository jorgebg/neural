from typhon.settings.basic import *
import os

AUTOINSTALLED_APPS += (
    'south',
    'tartarus.django.templatetags',
    'django.contrib.markup',
    'haystack',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'
    }
    #'default': {
    #    'ENGINE': 'xapian_backend.XapianEngine',
    #    'PATH': PROJECT_ROOT + 'index',
    #},
}