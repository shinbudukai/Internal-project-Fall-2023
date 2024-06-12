from .settings import *
import os

#Access system's getenvment
from dotenv import load_dotenv
load_dotenv()

ALLOWED_HOSTS = [os.getenv('WEBSITE_HOSTNAME')] if 'WEBSITE_HOSTNAME' in os.getenv else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.getenv['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.getenv else []

hostname = os.getenv['DBHOST']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv['DBNAME'],
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.getenv['DBUSER'],
        'PASSWORD': os.getenv['DBPASS'] 
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Enables whitenoise for serving static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False