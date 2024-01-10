from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, mixins
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from vinculos.serializers import *
from vinculos.models import *

class LocaisTrabalhoList(ReadOnlyModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class FuncoesList(ReadOnlyModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer
    

class TiposList(ReadOnlyModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


class TiposVinculoList(ReadOnlyModelViewSet):
    queryset = TipoVinculo.objects.all()
    serializer_class = TipoVinculoSerializer


class SexoList(ReadOnlyModelViewSet):
    queryset = Sexo.objects.all()
    serializer_class = SexoSerializer


class VinculosPendentesViewSet(ReadOnlyModelViewSet):
    queryset = Vinculo.objects.all().filter(status_ids_id=1)
    serializer_class = VinculosPendentesSerializer
    http_method_names = ['get', 'options', 'head', 'trace']
    
class VinculosViewSet(ModelViewSet):
    queryset = Vinculo.objects.all()
    serializer_class = VinculoSerializer


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    http_method_names = ['get', 'post', 'patch','options', 'head', 'trace']
    