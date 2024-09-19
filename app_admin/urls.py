from django.urls import path
from app_admin.views import caisse_dashboard, dashboard

urlpatterns =[

path("",dashboard.AdminDashboardView.as_view(), name="dashboard"),
path("caisse/",caisse_dashboard.CaisseDashboardView.as_view(), name="caisse"),

]