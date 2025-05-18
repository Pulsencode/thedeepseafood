import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", default=False)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

EXTERNAL_APPS = [
    "accounts.apps.AccountsConfig",
    "career.apps.CareerConfig",
    "products.apps.ProductsConfig",
    "administration.apps.AdministrationConfig",
    "company.apps.CompanyConfig",
    "phonenumber_field",
    "django.contrib.sitemaps",
    "django_summernote",
    "public_interface",
]

INSTALLED_APPS += EXTERNAL_APPS

LOGIN_URL = "login_view"

LOGIN_REDIRECT_URL = "admin_dashboard"

LOGOUT_REDIRECT_URL = "home"

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "public_interface.context_processors.global_context",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / "assets"

MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email configuration
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_DEBUG = os.getenv("EMAIL_DEBUG")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "verbose",
        },
        "test_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "test_logs.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True,
        },
        "test": {
            "handlers": ["test_file"],
            "level": "DEBUG",
            "propagate": False,  # Ensure logs don't propagate to the root or other loggers
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}


SUMMERNOTE_CONFIG = {
    "iframe": True,  # Use iframe for rendering
    "summernote": {
        "width": "100%",
        "height": "400px",
    },
    "toolbar": [
        ["style", ["style"]],
        ["font", ["bold", "italic", "underline", "clear"]],
        ["para", ["ul", "ol", "paragraph"]],
        ["table", ["table"]],
        ["view", ["fullscreen", "codeview", "help"]],
    ],
}


DATA_UPLOAD_MAX_MEMORY_SIZE = 200 * 1024 * 1024
CSRF_TRUSTED_ORIGINS = ["https://thedeepseafood.com"]
