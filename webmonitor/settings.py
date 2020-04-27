"""
Django settings for webmonitor project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@c*hlp1prhh5up^i9c9&0w86&@2!d)fb*r$up1cf!hhnlyf_@&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

# Application definition

INSTALLED_APPS = [
    'import_export', 'setting.apps.SettingConfig', 'task.apps.TaskConfig',
    'simpleui', 'django_apscheduler', 'django.contrib.admin',
    'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.messages',
    'django.contrib.staticfiles'
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
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

ROOT_URLCONF = 'webmonitor.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'webmonitor.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# SIMPLEUI 配置
SIMPLEUI_HOME_INFO = False
SIMPLEUI_CONFIG = {
    'system_keep':
    True,
    'menus': [{
        'name': '文档',
        'icon': 'fa fa-file',
        'url': 'https://www.logicjake.xyz/WebMonitor/'
    }],
    'menu_display': ['Simpleui', '任务管理', '设置', '文档'],
}

SIMPLEUI_ICON = {
    '系统邮箱': 'fas fa-mail-bulk',
    'RSS监控管理': 'fas fa-rss',
    '网页监控管理': 'far fa-file-code',
    '任务状态': 'far fa-calendar-check',
}

SIMPLEUI_ANALYSIS = False
SIMPLEUI_STATIC_OFFLINE = True

# logging配置
log_path = os.path.join(BASE_DIR, 'static', 'log')
log_file = os.path.join(log_path, 'log.txt')
if not os.path.exists(log_file):
    os.makedirs(log_path, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format':
            '%(asctime)s [%(threadName)s:%(thread)d] '
            '[%(module)s:%(funcName)s:%(lineno)d] [%(levelname)s]- %(message)s'
        }
    },
    'filter': {},
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': log_file,
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'main': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}
