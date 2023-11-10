from django.contrib import admin
from .models import Category, Product, Attribute, Item, ItemParameter, Vendor


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    search_fields = ["name"]


class AttributeInlines(admin.TabularInline):
    model = Attribute
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "id"]
    inlines = [AttributeInlines]
    search_fields = ["name"]
    autocomplete_fields = ["category"]


# @admin.register(Attribute)
# class AttributeAdmin(admin.ModelAdmin):
#     list_display = ["name", "id", "product"]


class ItemParameterInlines(admin.TabularInline):
    model = ItemParameter
    extra = 0

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "attribute":
            if getattr(request, "_product_instance", None) is not None:
                field.queryset = field.queryset.filter(
                    product=request._product_instance
                )
            else:
                field.queryset = field.queryset.none()
        return field


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["product", "id", "price", "count"]
    # Добавление поля для поисковой строки в Админке
    search_fields = ["product__name"]
    autocomplete_fields = ["product"]

    inlines = [ItemParameterInlines]

    def get_inlines(self, request, obj):
        if obj:
            return super().get_inlines(request, obj)
        else:
            return []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["product"]
        else:
            return super().get_readonly_fields(request, obj=None)

    def get_form(self, request, obj=None, **kwargs):
        request._product_instance = getattr(obj, "product", None)
        return super().get_form(request, obj, **kwargs)


# @admin.register(ItemParameter)
# class ItemParameterAdmin(admin.ModelAdmin):
#     list_display = ["attribute", "id", "item", "value"]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "owner"]
