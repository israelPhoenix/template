from django.views.generic import TemplateView

class LoginEtudiantView(TemplateView):
    template_name= 'public/pages/login_etudiant.html'