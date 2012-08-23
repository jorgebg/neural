from typhon.settings.basic import *
import os

AUTOINSTALLED_APPS += (
    'south',
    'tartarus.django.templatetags',
    'django.contrib.markup',
    'haystack',
    'compressor',
)

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