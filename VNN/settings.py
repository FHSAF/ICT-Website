from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#9okka7o^c$)yhp$q6!9w6sufss(ldwbytzs@=knh2u^n)y%&@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    'accounts',
    'pages',
    'contact',
    'django_email_verification',
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

ROOT_URLCONF = 'VNN.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'VNN.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'viradbms',
#         'USER': 'postgres',
#         'PASSWORD': 'miPass4Sd@123',
#         'HOST': 'localhost'
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kabul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'VNN/static')
]

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Messages
# MESSAGE_TAGS = {
#     messages.ERROR: 'danger'
# }


try:
    from .local_settings import *
except ImportError:
    pass

AUTH_USER_MODEL = 'accounts.UserProfile'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# def verified_callback(user):
#     user.is_active = True


# EMAIL_VERIFIED_CALLBACK = verified_callback

# EMAIL_ACTIVE_FIELD = 'is_acitve'
# EMAIL_SERVER = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_ADDRESS = 'fedasameh2018@gmail.com'
# EMAIL_FROM_ADDRESS = 'fedasameh2018@gmail.com'
# EMAIL_PASSWORD = 'snxyfjgvmwjhhcqo'
# EMAIL_MAIL_SUBJECT = 'CONFIRM YOUR EMAIL'
# EMAIL_MAIL_HTML = 'mail_body.html'
# EMAIL_MAIL_PLAIN = 'mail_body.txt'
# EMAIL_TOKEN_LIFE = 60 * 60
# EMAIL_PAGE_TEMPLATE = 'c_template.html'
# EMAIL_PAGE_DOMAIN = 'http://10.100.100.222:8000'


# # For Django Email Backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# # EMAIL_PORT = 587
# EMAIL_HOST_USER = 'fedasameh2018@gmail.com'
# # os.environ['password_key'] suggested
# EMAIL_HOST_PASSWORD = 'snxyfjgvmwjhhcqo'
# # EMAIL_USE_TLS = True

def verified_callback(user):
    user.is_verified = True


EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = 'admin_local@mydomain.com'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'partials/_mail_body.html'
EMAIL_MAIL_PLAIN = 'mail_body.txt'
EMAIL_TOKEN_LIFE = 60 * 60
EMAIL_PAGE_TEMPLATE = 'Form/login_form.html'
EMAIL_PAGE_DOMAIN = 'https://mydomain.com'

# For Django Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.mydomain.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'admin@mydomain.com'
EMAIL_HOST_PASSWORD = 'LLK@!@7712jdsi@@'  # '&hMY]4(j[;i@'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'viranoreply@gmail.com'
# EMAIL_HOST_PASSWORD = '>>P@5w0rd<<'
