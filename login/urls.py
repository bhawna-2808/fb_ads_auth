from django.urls import path, include
from . import views
app_name = 'login'

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('privacy-policy', views.privacy, name='privacy-policy'),
    path('terms-condition', views.terms, name='terms-condition')
]
