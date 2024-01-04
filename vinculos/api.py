from django.shortcuts import get_object_or_404
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

class FuncionarioAPIList(APIView):
    def get(self, request: Request) -> Response:
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(instance=funcionarios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = FuncionarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FuncionarioAPI(APIView):
    def get(self, request: Request, pk: int) -> Response:
        funcionario = get_object_or_404(Funcionario.objects.all(), pk=pk)
        serializer = FuncionarioSerializer(instance=funcionario, many=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    