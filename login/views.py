from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.utils import psa
from social_core.exceptions import AuthCanceled
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import login
# Create your views here.

import logging
logger = logging.getLogger(__name__)


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

def privacy(request):
    return render(request, 'privacy_policy.html')


def terms(request):
    return render(request, 'terms.html')


@psa('social:complete')
def social_auth_complete(request, backend):
    try:
        user = request.backend.auth_complete()
    except AuthCanceled:
        # Handle the case where authentication was canceled
        return HttpResponse("Authentication canceled. Please try again.")
    except Exception as e:
        # Log the exception for further investigation
        logger.error(f"Exception during social authentication: {str(e)}")
        return HttpResponse("An error occurred during authentication. Please try again later.")
    
    if user:
        # Successful authentication, handle user session or redirect
        login(request, user)
        return redirect('home')  # Replace 'home' with your desired redirect URL name
    else:
        # Handle case where user is not authenticated
        return HttpResponse("Authentication failed. Please try again.")