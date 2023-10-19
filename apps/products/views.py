from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from apps.products.models import Item
from apps.products.serializers import DetailItemSerializer, ItemSerializer
from apps.users.permissions import IsVendor
from apps.products import service_HTTP
from apps.products import service


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated, IsVendor])
def import_data(request):
    name_format = request.query_params.get("file_name", "name.csv")
    list(name_format)

    name_file, data_format = name_format.rsplit(".")
    owner_id = request.user.id

    try:
        service_HTTP.import_data(name_file, data_format, owner_id)
    except FileNotFoundError:
        raise ValidationError("incorrect file name", code="incorrect-file-name")

    return Response(status=status.HTTP_201_CREATED)


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated, IsVendor])
def import_file(request):
    # data_format = request.query_params.get("file_type", "csv")
    if not request.FILES or "file" not in request.FILES:
        raise ValidationError("no file", code="no-file")
    data_stream = request.FILES["file"]

    temp_list = list(data_stream.name)
    for i in temp_list:
        if i == ".":
            count = temp_list.index(i) + 1
    data_format = "".join(temp_list[count:])

    service.import_data(data_stream, data_format, request.user.id)
    return Response(status=status.HTTP_201_CREATED)


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = DetailItemSerializer

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]  # DjangoFilterBackend - сортировка по параметру. Не указали конкретный параметр, поэтому можно сортировать по всем параметрам нашей модели - Item

    filterset_fields = ["product__category"]  # Фильтр по id Категории
    search_fields = ["product__name"]
    pagination_class = LimitOffsetPagination

    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return ItemSerializer
    #     return DetailItemSerializer
