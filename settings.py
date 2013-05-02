# -*- coding: utf-8 -*-
# Django settings for whois-iepathos.rhcloud.com
# Written by Glen Baker - iepathos@gmail.com
import imp, os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True
    DEBUG = False
else:  
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Glen Baker', 'iepathos@gmail.com'),
)
MANAGERS = ADMINS

if ON_OPENSHIFT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.environ['OPENSHIFT_APP_NAME'],  # Or path to database file if using sqlite3.
            'USER': os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],                      # Not used with sqlite3.
            'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],                  # Not used with sqlite3.
            'HOST': os.environ['OPENSHIFT_MYSQL_DB_HOST'],                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': os.environ['OPENSHIFT_MYSQL_DB_PORT'],                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.path.join(PROJECT_DIR, 'dev.db'),  # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

if ON_OPENSHIFT:
    MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', 'media')
else:
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '..', 'static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make a dictionary of default keys
default_keys = { 'SECRET_KEY': '##############' }

# Replace default keys with dynamic values if we are in OpenShift
use_keys = default_keys
if ON_OPENSHIFT:
    imp.find_module('openshiftlibs')
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)

# Make this unique, and don't share it with anybody.
SECRET_KEY = use_keys['SECRET_KEY']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

if not ON_OPENSHIFT:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

ROOT_URLCONF = 'openshift.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

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

###################### Authentication ###############################
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.google.GoogleBackend',

    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

if ON_OPENSHIFT:
    USERENA_MUGSHOT_GRAVATAR_SECURE = True
    USERENA_USE_HTTPS = True
GRAVATAR_DEFAULT_URL = ''

################### Social Authentication ###########################
SOCIAL_AUTH_ENABLED_BACKENDS = ('twitter', 'facebook', 'linkedin', 'google',)

TWITTER_CONSUMER_KEY    = ''
TWITTER_CONSUMER_SECRET = ''
FACEBOOK_APP_ID         = ''
FACEBOOK_API_SECRET     = ''
LINKEDIN_CONSUMER_KEY   = ''
LINKEDIN_CONSUMER_SECRET= ''
GOOGLE_CONSUMER_KEY     = ''
GOOGLE_CONSUMER_SECRET  = ''
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_USER_MODEL = 'accounts.MyProfile'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'social_auth.backends.pipeline.user.create_user',
    #'custom_registration.social_auth.pipeline.create_profile',
    #'custom_registration.social_auth.pipeline.set_guardian_permissions',
    #'social_auth.backends.pipeline.social.associate_user',
    #'social_auth.backends.pipeline.social.load_extra_data',
    'auth_pipeline.pipeline.social_associate_and_load_data',
    'social_auth.backends.pipeline.user.update_user_details',
    #'auth_pipeline.pipeline.get_user_avatar',
    'auth_pipeline.pipeline.get_user_gender',
    'auth_pipeline.pipeline.get_user_location',
    'auth_pipeline.pipeline.get_user_fullname',
)

SOCIAL_AUTH_UID_LENGTH = 223 # MySQL uid max_length 767 byte limit
SOCIAL_AUTH_UUID_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 40 # MySQL salt max length
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 18
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 223

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
#import random
#SOCIAL_AUTH_DEFAULT_USERNAME = lambda: random.choice(['Darth Vader', 'Obi-Wan Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])

SOCIAL_AUTH_SLUGIFY_USERNAMES = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

TEMPLATE_CONTEXT_PROCESSORS += (
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

########################### Email ###################################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[whois-iepathos]'
#SERVER_EMAIL = 'iepathos@whois-iepathos.rhcloud.com'

#################### Beachmint Directory App ########################
# Base directory for Acme Directory App Storage
if ON_OPENSHIFT:
    BASE_DIRECTORY_PATH = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'media', 'directory')
else:
    BASE_DIRECTORY_PATH = os.path.join(PROJECT_DIR, 'media', 'directory')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'django_extensions',
    'core',

    'crispy_forms',
    'floppyforms',

    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
    'userena.contrib.umessages', # userena messaging system
    'admin_honeypot',

    'social_auth',

    # Beachmint Technical Exam
    'directory',
    'jewelry',
)

######################## Debug Toolbar ##############################
if not ON_OPENSHIFT:
    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INTERNAL_IPS = ('127.0.0.1',)

###################### Activity Stream ##############################
"""
ACTSTREAM_SETTINGS = {
    'MODELS': ('auth.user', 'accounts.profile', 'auth.group', 'sites.site', 'comments.comment'),
    'MANAGER': 'actstream.managers.ActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}
"""

######################### Logging #################################
if not ON_OPENSHIFT:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
