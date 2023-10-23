from rest_framework import serializers

from apps.basket.models import BasketRow
from apps.products.serializers import ItemSerializer


class BasketRowSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BasketRow
        fields = ['id', 'item', 'item_id', 'qty']
