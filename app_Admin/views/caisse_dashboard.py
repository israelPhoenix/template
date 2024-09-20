from django.views.generic import TemplateView


class CaisseDashboardView(TemplateView):
    template_name = "admin_school/pages/services/caisse.html"