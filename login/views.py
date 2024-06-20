from django.shortcuts import render, redirect
from social_django.utils import load_strategy
from social_django.models import UserSocialAuth


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:
        try:
            # Get the user's social authentication instance for Facebook (example)
            facebook_auth = request.user.social_auth.get(provider='facebook')
            
            # Access specific details from the social authentication
            provider = facebook_auth.provider
            uid = facebook_auth.uid
            extra_data = facebook_auth.extra_data
            # Use the access token or other data as needed
            
            return render(request, 'home.html', {
                'provider': provider,
                'uid': uid,
                'extra_data': extra_data,
            })
        
        except UserSocialAuth.DoesNotExist:
            # Handle case where user did not authenticate via Facebook or any other provider
            pass
    
    return render(request, 'home.html')
# def home(request):
#     if request.user.is_authenticated:
#         social = request.user.social_auth.get(provider='facebook')
#         access_token = social.extra_data['access_token']
#         # Use the access token to make API calls to Facebook
#     return render(request, 'home.html')


def logout(request):
    logout(request)
    return redirect('login') 