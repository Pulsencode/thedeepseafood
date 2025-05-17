from .base import *  # noqa: F401, F403

"""
Production settings for the Django project.
This module contains the settings and configuration for the production environment.
It imports the base settings and overrides specific settings for production use.
Settings:
- DEBUG: Set to False to disable debug mode.
- ALLOWED_HOSTS: List of allowed host/domain names for this Django site.
- FILE_UPLOAD_MAX_MEMORY_SIZE: Maximum size (in bytes) for file uploads.
- DATA_UPLOAD_MAX_MEMORY_SIZE: Maximum size (in bytes) for data uploads.
- SECURE_SSL_REDIRECT: Redirect all non-HTTPS requests to HTTPS.
- SESSION_COOKIE_SECURE: Use a secure cookie for the session cookie.
- CSRF_COOKIE_SECURE: Use a secure cookie for the CSRF cookie.
- SECURE_BROWSER_XSS_FILTER: Enable the browser's XSS filtering protection.
Database Configuration:
- DATABASES: Dictionary containing the database configuration.
    - ENGINE: Database backend to use (MySQL in this case).
    - NAME: Database name, retrieved from environment variables.
    - USER: Database user, retrieved from environment variables.
    - PASSWORD: Database password, retrieved from environment variables.
    - HOST: Database host, retrieved from environment variables.
    - PORT: Database port, retrieved from environment variables.
    - OPTIONS: Additional options for the database connection.
"""

DEBUG = False

ALLOWED_HOSTS = [
    " ",  # Need to replace this with the server IP
    "localhost",
]  # Example - Need to Replace with the server IP - Do not remove localhost

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB (in bytes)

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB (in bytes)

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

# Database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.getenv("NAME"),  # noqa: F405
#         "USER": os.getenv("USER"),  # noqa: F405
#         "PASSWORD": os.getenv("PASSWORD"),  # noqa: F405
#         "HOST": os.getenv("HOST"),  # noqa: F405
#         "PORT": os.getenv("PORT"),  # noqa: F405
#         "OPTIONS": {
#             "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("NAME"),  # noqa: F405
        "USER": os.getenv("USER"),  # noqa: F405
        "PASSWORD": os.getenv("PASSWORD"),  # noqa: F405
        "HOST": os.getenv("HOST"),  # noqa: F405
        "PORT": os.getenv("PORT"),  # noqa: F405
    }
}
