from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated,]


class VinculosPendentesViewSet(ReadOnlyModelViewSet):
    queryset = Vinculo.objects.all().filter(status_ids_id=1)
    serializer_class = VinculosPendentesSerializer
    http_method_names = ['get', 'options', 'head', 'trace']
    permission_classes = [IsAuthenticated,]
    

class VinculosCNESViewSet(ReadOnlyModelViewSet):
    queryset = Vinculo.objects.all().filter(status_cnes_id=1)
    serializer_class = VinculosPendentesSerializer
    http_method_names = ['get', 'options', 'head', 'trace']
    permission_classes = [IsAuthenticated,]


class AllVinculosViewSet(ReadOnlyModelViewSet):
    queryset = Vinculo.objects.all()
    serializer_class = VinculosPendentesSerializer
    http_method_names = ['get', 'options', 'head', 'trace']
    permission_classes = [IsAuthenticated,]

    
class VinculosViewSet(ModelViewSet):
    queryset = Vinculo.objects.all()
    serializer_class = VinculoSerializer
    permission_classes = [IsAuthenticated,]


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    http_method_names = ['get', 'post', 'patch','options', 'head', 'trace']
    permission_classes = [IsAuthenticated,]
