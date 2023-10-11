from django.contrib import admin
from django.urls import path, include

from apps.products.views import import_data, import_file

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path("api/v1/import-data/", import_data),
    path("api/v1/import-file/", import_file),
]
