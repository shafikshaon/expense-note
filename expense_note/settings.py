from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Retrieving DEBUG mode from environment variable, defaulting to False if not provided
DEBUG = config("DEBUG", default=False, cast=bool)

if DEBUG:
    from .development import *
else:
    from .production import *

ROOT_URLCONF = "expense_note.urls"

WSGI_APPLICATION = "expense_note.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
