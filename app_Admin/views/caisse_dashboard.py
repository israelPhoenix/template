from django.views.generic import TemplateView
from app_caisse.models import Entrecaisse
from app_caisse.models import Sortiecaisse
from django.shortcuts import render


class CaisseDashboardView(TemplateView):
    template_name = "admin_school/pages/caisse.html"

    def post(self,request):
        if request.method =='POST':
            entre = Entrecaisse(
                montant = request.POST['montant'],
                libelle =request.POST['libelle'],
            )

            entre.save()
            return self.render_to_response(self.get_context_data(success_message="Enregistrement reussie !"))

    # def post_sortie(self,request):
    #     if request.method =='POST':
    #         sortie = Sortiecaisse(
    #             montant = request.POST['montant_sortie'],
    #             libelle =request.POST['libelle_sortie'],
    #         )
    #         sortie.save()
    #         return self.render_to_response(self.get_context_data(success_message="Inscription réussie !"))

    # def post(self, request):
    #     if request.method == 'POST':
    #         forms = {
    #             'entre': Entrecaisse(
    #                 montant=request.POST['montant'],
    #                 libelle=request.POST['libelle'],
    #             ),
    #             'sortie': Sortiecaisse(
            #         montant=request.POST['montant_sortie'],
            #         libelle=request.POST['libelle_sortie'],
            #     ),
            # }
            #
            # for form_name, form in forms.items():
            #     form.save()
            #     # Vous pouvez ajouter ici des messages de succès personnalisés en fonction de form_name
            #
            # return self.render_to_response(self.get_context_data(success_message="Enregistrement réussi !"))

    def get (self,request):
        aff_entre = Entrecaisse.objects.all()
        aff_sortie = Sortiecaisse.objects.all()


        context ={
        'aff_entre': aff_entre,
            'aff_sortie': aff_sortie,
        }
        return render(request, self.template_name, context)




