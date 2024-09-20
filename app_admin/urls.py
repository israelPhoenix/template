from django.urls import path
from .views import caisse_dashboard, dashboard


urlpatterns =[

        path("", dashboard.AdminDashboardView.as_view(), name="dashboard"),
        path("caisse/", caisse_dashboard.CaisseDashboardView.as_view(), name="caisse"),

]