"""trainingcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ondr.li"
admin.site.site_title = "ondr.li"
admin.site.index_title = "Welcome to ondr.li"

SITE_HEADER_SUFFIX = os.environ.get("SITE_HEADER_SUFFIX")
if SITE_HEADER_SUFFIX:
    admin.site.site_header += " %s" % SITE_HEADER_SUFFIX
    admin.site.site_title += " %s" % SITE_HEADER_SUFFIX

urlpatterns = [
    path("", include("django_prometheus.urls")),
    path("", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
