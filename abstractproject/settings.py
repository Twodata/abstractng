"""
Django settings for abstractproject project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("ABSTRACT_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
        'www.abstract.ng',
        '127.0.0.1'
        ]



# Email settings for PRODUCTION PURPOSE

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#SEND_GRID_API_KEY = ''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get("ABSTRACT_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True



# Application definition

INSTALLED_APPS = [
    'journal',
    'registration', # add registration package
    'django.contrib.admin',    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps', # added for sitemap xml
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'widget_tweaks',  # form tweaking app
    'el_pagination', # pagination app
    'ckeditor',  #  text editor app
    'ckeditor_uploader',    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'abstractproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'abstractproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : os.environ.get("ABSTRACT_DB_NAME"),
        'USER' : 'postgres',
        'PASSWORD' : os.environ.get("DB_PASSWORD"),
        'HOST' : '127.0.0.1',
        'PORT' :'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


ADMINS = (
        ('Osabohien', 'osabohienchukwuma@gmail.com'),
        )   # added for deployment purposes

MANAGERS = ADMINS   # added for deployment purposes



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# django-registration-redux package variables
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 28
REGISTRATION_AUTO_LOGIN = True

LOGIN_REDIRECT_URL = '/journal/'
LOGIN_URL = '/accounts/login/'
SITE_ID = 1

DATE_INPUT_FORMAT = ['%d %B, %Y']



# settings for pagination app

EL_PAGINATION_PER_PAGE = 20
EL_PAGINATION_PER_LABEL = 'page'
EL_PAGINATION_PREVIOUS_LABEL ='<<'
EL_PAGINATION_NEXT_LABEL = '>>'
EL_PAGINATION_FIRST_LABEL = 'firstpage'
EL_PAGINATION_LAST_LABEL = 'lastpage'
EL_PAGINATION_ADD_NOFOLLOW = False
EL_PAGINATION_PAGE_LIST_CALLABLE = None
EL_PAGINATION_DEFAULT_CALLABLE_EXTREMES = 3
EL_PAGINATION_DEFAULT_CALLABLE_AROUNDS = 2
EL_PAGINATION_DEFAULT_CALLABLE_ARROWS = False
EL_PAGINATION_USE_NEXT_PREVIOUS_LINKS = True



# Text editor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '/static/js/jquery-3.3.1.js' 


CKEDITOR_CONFIGS = {
'default': {
'width':'100%',
'removePlugins' : 'elementspath',
'resize_enabled' : False,
'toolbar': 'Custom',
'toolbar_Custom': [
['Bold', 'Italic', 'Underline', 'Strike','Subscript','Superscript'], 
[ 'TextColor','BGColor' ], ['Undo', 'Redo'],
['NumberedList', 'BulletedList','-', 'Blockquote'],['Cut', 'Copy', 'Paste'],
['Link', 'Unlink'], ['Image','Table','HorizontalRule','Smiley','SpecialChar'],[ 'Maximize']
]

  },

'review_toolbar': {
'width' : '100%',
'height' : '50%',
'removePlugins' : 'elementspath',
'resize_enabled' : False,
'toolbar': 'Custom',
'toolbar_Custom': [
['Bold', 'Italic', 'Underline'],
['Link', 'Unlink'], ['Blockquote'], ['Undo', 'Redo'], ['Image','Smiley','SpecialChar'], [ 'Maximize']
],

  },

}



  
