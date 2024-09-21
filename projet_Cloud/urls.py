from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("app_Public.urls")),

    path("admin/", admin.site.urls),
    # admin
    #  il faut toujours inclure les urls des apps comme app_Admin.urls
    #  selon les apps definit dans le projet
    path("dashboard-admin/", include("app_Admin.urls")),


]
