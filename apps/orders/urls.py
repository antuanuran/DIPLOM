from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.orders.views import checkout
from apps.products.views import ItemViewSet, import_data, import_file


urlpatterns = [path("checkout/", checkout)]
