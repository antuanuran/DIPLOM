from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from rest_framework import status


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated])
def checkout(request):
    user = request.user
    basket = request.user.baskets.first()
    if not basket:
        raise ValidationError("user hasn't basket", code="no-basket")

    if not basket.rows.exists():
        raise ValidationError("user hasn't products in the basket", code="no-products-in-basket")

    for row in basket.rows.all():
        if row.qty > row.item.count:
            raise ValidationError(f"item is out of stock - {row.item.product.name}", code="no-products-in-basket")

    # код не безопасный: добавить транзакций
    order = Order.objects.create(user=user)
    # неоптимальный код: сделать балк создание
    for row in basket.rows.all():
        order.rows.create(item=row.item, qty=row.qty, price=row.item.price)

    basket.rows.all().delete()  # Очищаем корзину

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
