from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from vinculos.serializers import *
from vinculos.models import *

@api_view()
def vinculos_api_view(request: Request) -> Response:
    vinculos = Vinculo.objects.all().filter(status_ids_id=1)
    serializer = VinculoSerializer(instance=vinculos, many=True)
    return Response(status=200, data=serializer.data)