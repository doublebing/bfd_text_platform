# -*- coding: utf-8 -*-
"""
Django settings for nlpshow project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_URL = 'http://nlp.api.baifendian.com'
NLP_TOKEN = '2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40'
#默认的日期和时间展示格式
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d G:i:s'

#默认的日期时间输入格式，可以有多个
DATETIME_INPUT_FORMATS = ('%Y-%m-%d %H:%M:%S',)

NLP_APIS = {"keywords": "keywords",
            "auto_summary": "auto_summary",
            "media_label":"media_label",
            "item_label":"item_label",
            "sentiment_weibo":"sentiment/weibo",
            "sentiment_auto":"sentiment/auto",
            "sentiment_news":"sentiment/news",
            "sentiment_finance":"sentiment/finance",
            "reputation":"reputation/get_result",
        }

cars = ['car_1_1','car_1_2','car_1_3']
mobiles = ['mobile_1_1','mobile_1_2','mobile_1_3']



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '25qq+kb*v4#grd9d%olt_u43u-o%#hk0gz3mba(z!(^nrbdx4y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nlpdemo',
    'account',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'nlpshow.urls'

WSGI_APPLICATION = 'nlpshow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'userinfo_manage',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'192.168.80.44',
        'PORT':'3306',
    }
}

REDIS_HOSTS = '192.168.80.44'
REDIS_PORT = 6379





# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'demo',
#         'USER':'root',
#         'PASSWORD':'root',
#         'HOST':'127.0.0.1',
#         'PORT':'3306',
#     }
# }
#
# REDIS_HOSTS = '127.0.0.1'
# REDIS_PORT = '6379'



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = 'nlpdemo.user'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

#TEMPLATE zh_CN
FILE_CHARSET='utf-8'
DEFAULT_CHARSET='utf-8'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'complete': {
            'format': '[%(levelname)s %(asctime)s @ %(process)d] (%(pathname)s/%(funcName)s:%(lineno)d) - %(message)s'
        },
        'online': {
            'format': '[%(levelname)s %(asctime)s @ %(process)d] - %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'online',
            'filename' : os.path.join(BASE_DIR, 'log/errors.log').replace('\\','/')

        },
        'pt_log_file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'complete',
            'filename' : os.path.join(BASE_DIR, 'log/nlp_demo.log').replace('\\','/')

        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'complete'
        },

    },
    'loggers': {
        '': {
            'handlers':['file'],
            'propagate': False,
            'level':'DEBUG',
        },
        'nlp_view_log': {
            'handlers':['pt_log_file', 'console'],
            'propagate': False,
            'level':'INFO',
        },
    }
}
