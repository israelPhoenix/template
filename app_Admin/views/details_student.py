from django.views.generic import TemplateView
from app_Inscription.models import Inscription
from app_cycle.models import Filiere, Cycle, Promotion
from django.shortcuts import render, get_object_or_404
class DetailEtudiantView(TemplateView):
    template_name= 'admin_school/pages/details_etudiant.html'
    model = Inscription

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        profil = get_object_or_404(Inscription, pk=pk)
        context['profil'] = profil
        return context