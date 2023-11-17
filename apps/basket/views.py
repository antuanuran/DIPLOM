from rest_framework.viewsets import ModelViewSet
from apps.basket.models import BasketRow, Basket
from apps.basket.serializers import BasketRowSerializer


class BasketRowViewSet(ModelViewSet):
    queryset = BasketRow.objects.all()
    serializer_class = BasketRowSerializer

    def perform_create(self, serializer):
        basket, _ = Basket.objects.get_or_create(user_id=self.request.user.id)
        # print("2. perform_create - Перед сохранением")
        serializer.save(basket_id=basket.id)
