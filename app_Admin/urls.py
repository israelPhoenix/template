from django.urls import path
from .views import caisse_dashboard, dashboard, comptable, gestion_etudiants, login_admin, details_student, gestion_personel, prof, logout




urlpatterns =[

        path("", dashboard.AdminDashboardView.as_view(), name="dashboard"),
        path("caisse/", caisse_dashboard.CaisseDashboardView.as_view(), name="caisse"),
        path("comptable/", comptable.ComptableView.as_view(), name="comptable"),
        path("gestion_etudiant/", gestion_etudiants.EtudiantView.as_view(), name="etudiant"),
        path("login_admin/", login_admin.LoginAdminView.as_view(), name="login-admin"),
        path("details_etudiant/<str:pk>/", details_student.DetailEtudiantView.as_view(), name="details_etudiant"),
        path("gestion_personnel/", gestion_personel.PersonnelView.as_view(), name="gestion_personnel"),
        path("gestion_enseignant/", prof.ProfView.as_view(), name="enseignant"),
        path("logout_admin/", logout.logoutAdminView.as_view(), name="logout"),







]