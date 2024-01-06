from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from vinculos.serializers import *
from vinculos.models import *

class VinculosViewSet(ModelViewSet):
    queryset = Vinculo.objects.all().filter(status_ids_id=1)
    serializer_class = VinculoSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class FuncionarioAPI(APIView):
    def get(self, request: Request, pk: int) -> Response:
        funcionario = get_object_or_404(Funcionario.objects.all(), pk=pk)
        serializer = FuncionarioSerializer(instance=funcionario, many=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    