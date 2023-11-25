from rest_framework.viewsets import ModelViewSet
from apps.basket.models import BasketRow, Basket
from apps.basket.serializers import BasketRowSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema, no_body


@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description='Необходимо ввести только 2 параметра: {"qty": 1, "tovar_id": 1}',
    ),
)
class BasketRowViewSet(ModelViewSet):
    queryset = BasketRow.objects.all()
    serializer_class = BasketRowSerializer

    def perform_create(self, serializer):
        basket, _ = Basket.objects.get_or_create(user_id=self.request.user.id)
        # print("2. perform_create - Перед сохранением")
        serializer.save(basket_id=basket.id)
