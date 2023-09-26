from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.products.views import import_data

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/import-data/", import_data),
]
