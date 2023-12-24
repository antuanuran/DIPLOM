from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include("Diplom.urls_docs")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/", include("apps.products.urls")),
    path("api/v1/", include("apps.basket.urls")),
    path("api/v1/", include("apps.orders.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     from django.conf.urls.static import static
#
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
