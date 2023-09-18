from django.contrib import admin
from .models import Category, Product, Attribute, Item, ItemParameter, Vendor
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'id']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'product']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'id', 'price', 'count']


@admin.register(ItemParameter)
class ItemParameterAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'id', 'item', 'value']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'owner']
