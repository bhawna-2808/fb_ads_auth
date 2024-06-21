from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns = [
    path("", views.home, name='home'),

    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('privacy-policy', views.privacy, name='privacy-policy'),
    path('terms-condition', views.terms, name='terms-condition'),
    path('oauth/complete/facebook/', views.social_auth_complete, name='social_auth_complete'),

]
