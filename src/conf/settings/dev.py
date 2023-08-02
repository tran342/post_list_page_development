from django.conf import settings

from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.PROJECT_ROOT + '/dev.db',  # Switch to file for persistence
    }
}

LOGGING['loggers'] = {
    'app': {
        'handlers': ['console'],
        'propagate': True,
    }
}

