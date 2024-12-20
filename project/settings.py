import os

from environs import Env

env = Env()
env.read_env('.env.diary')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR + '/datacenter', os.getenv('DATABASE_NAME'))
    }
}

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
