from django.urls import path

from app_Public.views import home
from .views import home

urlpatterns = [

 path("", home.HomeView.as_view(), name="home"),

    ]