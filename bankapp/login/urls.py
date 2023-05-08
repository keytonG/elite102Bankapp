from django.urls import path, include
from django.shortcuts import redirect
from . import views

app_name="login"
urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login, name="login"),
    path("signupRedirect/", views.signupRedirect, name="signupRedirect"),
    path("signup/", views.signup, name="signup")
]