from pathlib import Path
import os
import dj_database_url
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key')

DEBUG = False

ALLOWED_HOSTS = ['*']


# =========================
# APPS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    'corsheaders',
    'my_app',
]


# =========================
# MIDDLEWARE (ВАЖНО)
# =========================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ДОЛЖЕН БЫТЬ ПЕРВЫМ

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
]


# =========================
# CORS FIX (ГЛАВНОЕ ИСПРАВЛЕНИЕ)
# =========================

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://dairyy2-ebo8kfjof-azizmamidov774s-projects.vercel.app",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"https://.*\.vercel\.app",
]

# ❌ БЫЛО ОШИБКОЙ: "PATCH" "PUT"
# ✅ ИСПРАВЛЕНО:
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "OPTIONS",
    "PATCH",
    "PUT",
    "DELETE",
]

# ❌ НЕ ИСПОЛЬЗУЙ "*"
CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
    "accept",
    "origin",
    "user-agent",
    "x-requested-with",
]


# =========================
# REST FRAMEWORK
# =========================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}


SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=60),
}


# =========================
# DATABASE
# =========================
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# =========================
# AUTH
# =========================
AUTH_USER_MODEL = 'my_app.Users'
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']


# =========================
# STATIC / MEDIA
# =========================
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'