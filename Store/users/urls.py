from django.urls import path
from . import views

urlpatterns=[
    path('accounts/login/', views.login_user, name='Login'),
    path('accounts/register_user', views.register_user, name="register_user"),
]