from django.contrib import admin
from rest_framework.response import Response

from apps.basket.models import BasketRow, Basket
from rest_framework.exceptions import ValidationError


@admin.register(BasketRow)
class BasketRowAdmin(admin.ModelAdmin):
    list_display = ["basket", "item", "qty", "sum_basket_row"]

    autocomplete_fields = [
        "item",
        "basket",
    ]  # Добавление поля для поисковой строки в Админке. item - значит мы идём в Админку с Item и прописываем - search_fields = []

    def save_model(self, request, obj, form, change):
        if obj.qty > obj.item.count:
            raise ValidationError(f"Max Limit Value: {obj.item.count}")

        return super().save_model(request, obj, form, change)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "sum_basket"]
    readonly_fields = ["sum_basket"]
    search_fields = ["user__email"]

    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)
