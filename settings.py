# Django settings for doermann project.
import os
from django.conf.global_settings import *
from limbo.conf.secrets import ConfigSettings
cs = ConfigSettings(ConfigSettings.locals_config_path(__file__))

DEBUG = cs.getboolean('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG


CWD = os.path.dirname(__file__)

SYSTEM_APPNAME = cs.get('SYSTEM_APPNAME')

ADMINS = cs.items('ADMINS')

MANAGERS = cs.items('MANAGERS', ADMINS)

DATABASES = {
    'default': cs.group_dict('DB_DEFAULT')
}

TIME_ZONE = cs.get('TIME_ZONE')

LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = cs.get('MEDIA_ROOT', 'DIRS')
MEDIA_URL = cs.get('MEDIA_URL', 'DIRS')
STATIC_URL = 'static/'
ADMIN_MEDIA_PREFIX = cs.get('ADMIN_MEDIA_PREFIX', 'DIRS')
LOGIN_REDIRECT_URL = '/'
SECRET_KEY = cs.get('SECRET_KEY')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'limbo.context.page_context',
    'limbo.context.request_context',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'limbo.middleware.LoginMiddleware',
    'limbo.middleware.ExceptionsMiddleware',
    'limbo.middleware.RequestMiddleware',
    'limbo.middleware.PageMiddleware',
    'limbo.middleware.AdminDebugToolbarMiddleware',
)

ROOT_URLCONF = 'doermann.urls'

TEMPLATE_DIRS = (
    os.path.join(CWD, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'django.contrib.admin',
    'limbo',
    'south',
    'django_extensions',
    'registration',
    'doermann.resume',
) + cs.gettuple('APPS', 'TESTING') + cs.gettuple('PLUGIN_APPS')



JAVASCRIPTS = (
    "jquery.dataTables.js",
    "jquery.ui.combobox.min.js",
    "ui.multiselect.js",
    "jquery.ui.timepicker.min.js",
    "jquery.form.js",
    "fg.menu.js",
    "date.js",
    "jquery.gritter.js",
    "jquery.media.js",
    "autoresize.jquery.min.js",
    'rgbcolor.js',
    'jquery.masonry.min.js',
    'jquery.timeago.js',
)

STYLE_SHEETS = (
    "fg.menu.css",
    "ui.multiselect.css",
    "messages.css",
    "gritter.css",
    "ui-lightness/theme.css",
)

LESS_SHEETS = (
    "style.less",
    "site.less",
)


TEST_RUNNER = 'limbo.testing.AdvancedTestSuiteRunner'
TESTING_NOT_IMPLEMENTED_FAIL = cs.getboolean('NOT_IMPLEMENTED_FAIL', 'TESTING', True)
TEST_EXCLUDE = cs.getlist('EXCLUDE', 'TESTING')
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
ACCOUNT_ACTIVATION_DAYS = cs.getint('ACCOUNT_ACTIVATION_DAYS', 'REGISTRATION')
LOGIN_URL = '/accounts/login/'

