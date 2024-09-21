from django.views.generic import TemplateView

class LoginAdminView(TemplateView):
    template_name= 'admin_school/pages/login_admin.html'