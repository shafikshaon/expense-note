from decouple import config

__author__ = "Shafikur Rahman"

# Retrieving secret key from environment variable
SECRET_KEY = config(
    "SECRET_KEY", cast=str, default="8c8c&(lx2^$pssf05nc-u3wq+ci9rchjg0qb_7z9era)=3!by_"
)

# Set the unique identifier for the current site
SITE_ID = 1

# Retrieving allowed hosts from environment variable, defaulting to "127.0.0.1" if not provided
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1",
    cast=lambda v: [s.strip() for s in v.split(",")],
)

APPEND_SLASH = True
