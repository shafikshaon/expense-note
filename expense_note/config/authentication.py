__author__ = "Shafikur Rahman"

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Define the custom user model used for authentication
AUTH_USER_MODEL = "accounts.SystemUser"

# Define the authentication backends for the Django project
AUTHENTICATION_BACKENDS = (
    "accounts.backends.email_or_username_backend.EmailOrUsernameModelBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# Define the URL where users will be redirected after successful login
LOGIN_REDIRECT_URL = "/"

# Define the URL where users will be redirected after logging out
LOGOUT_REDIRECT_URL = "/login/"

LOGIN_URL = "/login/"

PASSWORD_RESET_URL = "/password_reset/"

PASSWORD_RESET_PASSWORD_FIELD_NAME = "password"

PASSWORD_RESET_EMAIL_FIELD_NAME = "email"

PASSWORD_RESET_EMAIL_ADDRESS = "<EMAIL>"

PASSWORD_RESET_PASSWORD_MIN_LENGTH = 8

PASSWORD_RESET_PASSWORD_MAX_LENGTH = 255

PASSWORD_RESET_PASSWORD_VALIDATORS = []
