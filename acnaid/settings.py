import os
from django.utils.translation import ugettext_lazy as _

# PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''
MEDIA_URL = '/site_media/'
MEDIA_ROOT = '/home/bartek/workspace/acnaid/site_media/'
# STATIC_ROOT = ''
# STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # cms
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'acnaid.urls'

WSGI_APPLICATION = 'acnaid.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.localflavor',  # so distribution points have pl names
    
    'acnaid',  # should be before cms to allow template overrides
    
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',

    'cms.plugins.file',
    # 'cms.plugins.flash',
    # 'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    # 'cms.plugins.snippet',
    # 'cms.plugins.teaser',
    'cms.plugins.text',
    # 'cms.plugins.video',

    # 3rd party
    'rosetta',
    'cmsplugin_plaintext',

    # from oliprox & dermaprofil
    'faq',
    'metatags',
    'stores',
    'contact',
    'news',

    # my own
    'cms_extensions',

)

# links to oliprox stores
DATABASE_ROUTERS = ['stores.dbrouters.StoresDbRouter'] 

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

from settings_local import *
from cms_settings import *

SECRET_KEY = 't6n)lywk$#c2_8xxd8ys(-(_5(hqx4-=hq(-(13iik5vo$qyvh'

CMS_SEO_FIELDS = True