__author__ = "Shafikur Rahman"

from decouple import config

# Internationalization settings
LANGUAGE_CODE = "en-us"

TIME_ZONE = config("TIME_ZONE", default="Asia/Dhaka", cast=str)

USE_I18N = True

USE_TZ = True
