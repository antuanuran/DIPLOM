from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products import service


@api_view(http_method_names=["post"])
def import_data(request):
    data_format = request.query_params.get("file_type", "csv")
    data_stream = request.files[0]
    service.import_data(data_stream, data_format)
    return Response(status=status.HTTP_201_CREATED)
