from django.core.exceptions import ObjectDoesNotExist

__author__ = "Shafikur Rahman"

from django.contrib.auth import get_user_model


class EmailOrUsernameModelBackend:
    """
    Custom authentication backend that allows
    authentication with either a username or an email address.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if "@" in username:
                user = get_user_model().objects.get(email=username)
            else:
                user = get_user_model().objects.get(username=username)
            if user.check_password(password):
                return user
        except ObjectDoesNotExist:
            pass  # User does not exist or password is incorrect
        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
