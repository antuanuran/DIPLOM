from rest_framework import serializers

from apps.products.models import Item, ItemParameter, Product, Vendor


class VendorSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        model = Vendor
        fields = ["id", "name", "owner"]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "category", "vendor"]


class ItemParameterSerializer(serializers.ModelSerializer):
    attribute = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = ItemParameter
        fields = ["id", "value", "attribute"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "product",
            "price",
            "count",
            "upc",
            "parameters",
        ]


class DetailItemSerializer(ItemSerializer):
    product = ProductSerializer(read_only=True)
    parameters = ItemParameterSerializer(read_only=True, many=True)
