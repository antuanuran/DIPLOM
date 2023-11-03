from django.contrib import admin

from apps.orders.models import Order, OrderRow


class OrderRowInLine(admin.TabularInline):
    model = OrderRow
    extra = 0
    # Добавление поля для поисковой строки в Админке
    autocomplete_fields = ["item"]
    readonly_fields = ["sum"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "status", "created_at", "updated_at", "sum"]
    readonly_fields = ["sum"]
    ordering = ["-created_at"]
    inlines = [OrderRowInLine]
