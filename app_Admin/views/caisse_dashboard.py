from django.views.generic import TemplateView

class CaisseDashboardView(TemplateView):
    template_name = "admin/pages/services/caisse.html"