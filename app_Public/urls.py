from django.urls import path

from .views import home, contact, about

urlpatterns = [

    path("", home.HomeView.as_view(), name="home"),
    path("contact/", contact.ContactView.as_view(), name="contact"),
    path("about/", about.AboutView.as_view(), name="about"),

]