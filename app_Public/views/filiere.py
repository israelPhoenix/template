from django.views.generic import TemplateView
from app_Inscription.models import Inscription
from app_cycle.models import Filiere
class FiliereView(TemplateView):
    template_name = "public/pages/filieres.html"

    def post(self, request, *args, **kwargs):
        # Récupère l'objet Service en fonction de la clé primaire (pk) fournie dans l'URL
        Filiere = self.get_object()
        if request.method == 'POST':
            # Crée un nouvel objet ServiceContact avec les données soumises
            inscription = Inscription(
                service =Filiere,  # Associe le contact au service
                full_name=request.POST.get('name'),  # Récupère le nom du formulaire
                email=request.POST.get('email'),  # Récupère l'email du formulaire
                phone_number=request.POST.get('numero'),  # Récupère le numéro de téléphone du formulaire
                message=request.POST.get('message'),  # Récupère le message du formulaire
            )
            # Sauvegarde le nouvel objet ServiceContact dans la base de données
            inscription.save()
            messages.success(request, f"Votre service {inscription.service} a été reservé avec succes")
            # Rend le template avec un indicateur de succès
            return render(request, self.template_name, {'services': service_id, 'success': True})
        # Rend le template avec les détails du service (cas non nécessaire ici, mais pour être complet)
        return render(request, self.template_name, {'services': service_id})