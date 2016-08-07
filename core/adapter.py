from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.shortcuts import resolve_url


class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        threshold = 90

        assert request.user.is_authenticated()
        if (request.user.last_login - request.user.date_joined).seconds < threshold:
            url = '/thanks/'
        else:
            url = settings.LOGIN_REDIRECT_URL
        return resolve_url(url)