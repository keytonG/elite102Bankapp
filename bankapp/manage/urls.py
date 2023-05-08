from django.urls import path
from . import views
from login.models import account

app_name="manage"
urlpatterns = [
    path("<int:account_id>", views.index, name='index'),
    path("deposit", views.deposit, name='deposit'),
    path("withdrawal", views.withdrawal, name='withdrawal')
]