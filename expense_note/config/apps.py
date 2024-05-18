__author__ = "Shafikur Rahman"
# List of installed Django apps
DJANGO_DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "core.apps.CoreConfig",
    "accounts.apps.AccountsConfig",
    "wallets.apps.WalletsConfig",
]

INSTALLED_APPS = DJANGO_DEFAULT_APPS + CUSTOM_APPS
