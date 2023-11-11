from django.contrib import admin
from rest_framework.exceptions import ValidationError

from apps.orders.models import Order, OrderRow


class OrderRowInLine(admin.TabularInline):
    model = OrderRow
    extra = 0
    readonly_fields = ["sum_order_row"]
    
        # Добавление поля для поисковой строки в Админке
    autocomplete_fields = ["item"]



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "status", "created_at", "updated_at", "sum_order"]
    readonly_fields = ["sum_order"]
    ordering = ["-created_at"]
    inlines = [OrderRowInLine]

    def save_model(self, request, obj, form, change):
        # print(obj.rows)
        # if obj.rows.qty > obj.rows.item.count:
        #     raise ValidationError(f"Max Limit Value: {obj.item.count}")
        return super().save_model(request, obj, form, change)
