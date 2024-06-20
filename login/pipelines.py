from social_core.backends.facebook import FacebookOAuth2
from social_django.utils import load_strategy
import requests
from django.utils import timezone

def save_tokens(backend, user, response, *args, **kwargs):
    if isinstance(backend, FacebookOAuth2):
        user.social_auth.get(provider=backend.name).extra_data['access_token'] = response.get('access_token')
        user.social_auth.get(provider=backend.name).extra_data['expires'] = response.get('expires_in')
        user.social_auth.get(provider=backend.name).save()

def refresh_token(backend, user, *args, **kwargs):
    if isinstance(backend, FacebookOAuth2):
        social = user.social_auth.get(provider=backend.name)
        token_expiry = social.extra_data.get('expires')
        if token_expiry and token_expiry < timezone.now():
            strategy = load_strategy()
            access_token = social.extra_data.get('access_token')
            response = requests.get(
                'https://graph.facebook.com/oauth/access_token',
                params={
                    'grant_type': 'fb_exchange_token',
                    'client_id': backend.setting('SOCIAL_AUTH_FACEBOOK_KEY'),
                    'client_secret': backend.setting('SOCIAL_AUTH_FACEBOOK_SECRET'),
                    'fb_exchange_token': access_token,
                },
                headers={'Accept': 'application/json'}
            )
            response_data = response.json()
            social.extra_data['access_token'] = response_data.get('access_token')
            social.extra_data['expires'] = response_data.get('expires_in')
            social.save()
