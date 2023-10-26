from rest_framework import serializers

from apps.basket.models import BasketRow, Item
from apps.products.serializers import ItemSerializer, ItemParameterSerializer, ProductSerializer
from rest_framework.exceptions import ValidationError


class DetailSerializer(ItemSerializer):
    parameters = ItemParameterSerializer(read_only=True, many=True)
    product = ProductSerializer(read_only=True)


class BasketRowSerializer(serializers.ModelSerializer):
    item = DetailSerializer(read_only=True)
    item_id = serializers.IntegerField(write_only=True)
    basket_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BasketRow
        fields = ["id", "basket_id", "qty", "item", "item_id"]

    def validate(self, attrs):
        temp = Item.objects.filter(id=attrs["item_id"])
        if not temp:
            raise ValidationError("incorrect item_id", code="no-file")
        else:
            return attrs
