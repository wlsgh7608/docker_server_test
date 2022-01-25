from .common import *



DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample',
        'USER': 'local',
        'PASSWORD': '1234',

        'HOST': '127.0.0.1',
        'PORT': '3306',

    }
}