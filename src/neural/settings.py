from tartarus.django.conf.settings.default import *
import os


INSTALLED_APPS += (
    PROJECT_NAME,
    'south',
    'tartarus.django.templatetags',
    'django.contrib.markup',
    'haystack',
    'compressor',
    'jqm'
)

ROOT_URLCONF = PROJECT_NAME+'.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)


#Auth
LOGIN_REDIRECT_URL = '/'

#Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'
    }
    #'default': {
    #    'ENGINE': 'xapian_backend.XapianEngine',
    #    'PATH': PROJECT_ROOT + 'index',
    #},
}


# Compressor
STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_OUTPUT_DIR = '_cache'