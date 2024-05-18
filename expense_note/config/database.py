__author__ = "Shafikur Rahman"

from decouple import config

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME", "life_track"),
        "USER": config("DB_USER", default="postgres"),
        "PASSWORD": config("DB_PASSWORD", "postgres"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default=5432, cast=int),
        "CONN_MAX_AGE": config("DB_CONN_MAX_AGE", default=86400, cast=int),
    }
}
