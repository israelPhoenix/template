from django.views.generic import TemplateView


class CaisseDashboardView(TemplateView):
    template_name = "admin_school/pages/caisse.html"