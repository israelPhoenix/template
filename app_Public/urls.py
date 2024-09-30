from django.urls import path

from .views import home, contact, about,filiere,news,login

urlpatterns = [

    path("", home.HomeView.as_view(), name="home"),
    path("contact/", contact.ContactView.as_view(), name="contact"),
    path("about/", about.AboutView.as_view(), name="about"),
    path("filieres/", filiere.FiliereView.as_view(), name="filieres"),
    path("news/", news.NewsView.as_view(), name="news"),

    # il faut toujpur definir les urls de view qui existe et quand de meme tu
    # le defini dans le template
    # path("login/", login.LoginEtudiantView.as_view(), name="login")

    path("login/", login.Login.as_view(), name="login")

]