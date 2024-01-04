from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from vinculos.serializers import *
from vinculos.models import *

class VinculosAPIList(APIView):
    def get(self, request: Request) -> Response:
        vinculos = Vinculo.objects.all().filter(status_ids_id=1)
        serializer = VinculoSerializer(instance=vinculos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
