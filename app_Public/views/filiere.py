from django.views.generic import TemplateView
from app_Inscription.models import Inscription
from app_cycle.models import Filiere
from django.shortcuts import render, get_object_or_404
class FiliereView(TemplateView):
    template_name = "public/pages/filieres.html"

    model = Filiere
    def get(self, request):
        filieres = Filiere.objects.all()

        context = {
            'filieres': filieres,
        }

        return render(request, self.template_name, context)



    def post(self, request, *args, **kwargs):
        # Récupère l'objet Service en fonction de la clé primaire (pk) fournie dans l'URL
        # context = super().get_context_data(**kwargs)
        # pk = self.kwargs["pk"]
        # filierses_id = get_object_or_404(Filiere, pk=pk)
        # filieres_id = Filiere.objects.all()
        if request.method == 'POST':
            filiere_id = request.POST.get('filiere_id')

            # Récupérer l'instance de Filiere correspondante
            filieres = get_object_or_404(Filiere, pk=filiere_id)
            # Crée un nouvel objet ServiceContact avec les données soumises
            inscription = Inscription(
                filiere = filieres,  # Associe la filiere à l'inscription
                name =request.POST.get('nom'),  # Récupère le nom du formulaire
                postnom = request.POST.get('postnom'),  # Récupère le nom du formulaire
                prenom = request.POST.get('postnom'),
                adresse =request.POST.get('adresse'),
                email=request.POST.get('email'),  # Récupère l'email du formulaire
                phone_number =request.POST.get('phone'),  # Récupère le numéro de téléphone du formulaire
                sexe = request.POST.get('sexe'),  # Récupère le message du formulaire
                promotion = request.POST.get('promotion'),
            )
            # Sauvegarde le nouvel objet ServiceContact dans la base de données
            inscription.save()

            context = {
                'inscription': inscription,
                'filieres': filieres ,
            }

        # Rend le template avec les détails du service (cas non nécessaire ici, mais pour être complet)
        return render(request, self.template_name)