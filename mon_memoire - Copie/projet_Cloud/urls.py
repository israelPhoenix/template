"""
URL configuration for projet_Cloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", include("app_Public.urls")),

    path("admin/", admin.site.urls),

    # path("dashboard-sec/", include("app_secretary.urls")),
    # # admin
    # path("dashboard-admin/", include("app_admin.urls")),
    # #
    # path("dashboard-student/", include("app_student.urls")),
    # #
    # path("dashboard-teacher/", include("app_teacher.urls")),
]
