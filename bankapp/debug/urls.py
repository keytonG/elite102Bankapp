from django.urls import path
from . import views

app_name="debug"
urlpatterns = [
    path("", views.index, name='index')
]