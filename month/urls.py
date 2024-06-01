from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month_int>", views.app_settings_with_number, name="app_settings"),
    path("<str:month_str>", views.app_settings, name="app_challenge")
]
