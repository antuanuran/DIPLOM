from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsVendor
from apps.products import service_HTTP
from apps.products import service


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated, IsVendor])
def import_data(request):
    name_format = request.query_params.get("file_name", "name.csv")
    list(name_format)

    data_format = name_format[-3:]
    name_file = name_format[0:-4]
    owner_id = request.user.id

    service_HTTP.import_data(name_file, data_format, owner_id)

    return Response(status=status.HTTP_201_CREATED)


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated, IsVendor])
def import_file(request):
    data_format = request.query_params.get("file_type", "csv")
    if not request.FILES:
        raise ValidationError("no file", code="no-file")
    data_stream = request.FILES["file"]
    service.import_data(data_stream, data_format, request.user.id)
    return Response(status=status.HTTP_201_CREATED)
