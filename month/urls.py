from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:app>", views.app_settings_with_number),
    path("<str:app>", views.app_settings, name="app_challenge")
]
