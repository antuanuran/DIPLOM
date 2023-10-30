from django.contrib import admin

from apps.basket.models import BasketRow


@admin.register(BasketRow)
class BasketRowAdmin(admin.ModelAdmin):
    list_display = ["basket", "item", "qty"]
