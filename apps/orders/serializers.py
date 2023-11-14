from rest_framework import serializers
from apps.orders.models import OrderRow, Order
from apps.products.serializers import ItemSerializer, ItemParameterSerializer, ProductSerializer


class DetailSerializer(ItemSerializer):
    parameters = ItemParameterSerializer(read_only=True, many=True)
    product = ProductSerializer(read_only=True)


class OrderRowSerializer(serializers.ModelSerializer):
    item = DetailSerializer(read_only=True)

    class Meta:
        model = OrderRow
        fields = ["id", "item", "qty", "price"]


class OrderSerializer(serializers.ModelSerializer):
    rows = OrderRowSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ["id", "rows", "status", "created_at", "updated_at"]