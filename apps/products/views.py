from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.products import service
from apps.users.permissions import IsVendor


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated, IsVendor])
def import_data(request):
    data_format = request.query_params.get("file_type", "csv")
    if not request.FILES:
        raise ValidationError("no file", code="no-file")
    data_stream = request.FILES["file"]
    service.import_data(data_stream, data_format, request.user.id)
    return Response(status=status.HTTP_201_CREATED)
