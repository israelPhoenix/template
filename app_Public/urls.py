from django.urls import path

from .views import home, contact, about,filiere,news

urlpatterns = [

    path("", home.HomeView.as_view(), name="home"),
    path("contact/", contact.ContactView.as_view(), name="contact"),
    path("about/", about.AboutView.as_view(), name="about"),
    path("filieres/", filiere.FiliereView.as_view(), name="filieres"),
    path("news/", news.NewsView.as_view(), name="news")

]