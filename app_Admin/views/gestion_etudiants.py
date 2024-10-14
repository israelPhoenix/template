from django.views.generic import TemplateView
from app_Inscription.models import Inscription
from django.shortcuts import render
from django.views.generic import TemplateView
from app_Inscription.models import Inscription
from app_cycle.models import Filiere, Cycle, Promotion
from django.shortcuts import render, get_object_or_404

class EtudiantView(TemplateView):
    template_name= 'admin_school/pages/gestion_etudiant.html'

    def get(self, request):
        etudiants = Inscription.objects.all()
        context = {
            'etudiants': etudiants,
        }
        return render(request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     # Cette méthode permet de récupérer le contexte commun pour GET et POST
    #     context = super().get_context_data(**kwargs)
    #     context['filieres'] = Filiere.objects.all()
    #     context['cycles'] = Cycle.objects.all()
    #     context['promotions'] = Promotion.objects.all()
    #
    #     # Si un message de succès est présent, l'ajouter au contexte
    #     success_message = kwargs.get('success_message', '')
    #     context['success_message'] = success_message
    #
    #     return context
    #
    # def get(self, request, *args, **kwargs):
    #     # Simplement afficher le formulaire d'inscription au départ
    #     return self.render_to_response(self.get_context_data())
    #
    # def post(self, request, *args, **kwargs):
    #     # Récupérer les informations du formulaire
    #     filiere_id = request.POST.get('filiere_id')
    #     cycle_id = request.POST.get('cycle')
    #     promotion_id = request.POST.get('promotion')
    #
    #     # Vérifiez l'existence des objets à l'aide de get_object_or_404
    #     filiere = get_object_or_404(Filiere, pk=filiere_id)
    #     cycle = get_object_or_404(Cycle, pk=cycle_id)
    #     promotion = get_object_or_404(Promotion, pk=promotion_id)
    #
    #     # Créez une nouvelle inscription
    #     inscription = Inscription(
    #         filiere=filiere,
    #         name=request.POST.get('nom'),
    #         postnom=request.POST.get('postnom'),
    #         prenom=request.POST.get('prenom'),
    #         adresse=request.POST.get('adresse'),
    #         email=request.POST.get('email'),
    #         phone_number=request.POST.get('phone'),
    #         genre=request.POST.get('sexe'),
    #         promotion=promotion,
    #         cycle=cycle,
    #     )
    #
    #     # Sauvegarde l'inscription dans la base de données
    #     inscription.save()
    #
    #     # Redirige avec un message de succès via le contexte
    #     return self.render_to_response(self.get_context_data(success_message="Inscription réussie !"))
