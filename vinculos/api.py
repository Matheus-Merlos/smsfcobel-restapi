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
