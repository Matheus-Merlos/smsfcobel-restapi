from rest_framework.routers import SimpleRouter
from django.urls import path, include
from vinculos import api

app_name = 'vinculos'

vinculos_router = SimpleRouter(trailing_slash=True)
vinculos_router.register('vinculos-pendentes', api.VinculosPendentesViewSet)

vinculos_router.register('funcionarios', api.FuncionarioViewSet, basename='funcionarios')
vinculos_router.register('locais-trabalho', api.LocaisTrabalhoList)
vinculos_router.register('funcoes', api.FuncoesList)
vinculos_router.register('tipos', api.TiposList)
vinculos_router.register('tipos-vinculo', api.TiposVinculoList)

vinculos_router.register('', api.VinculosViewSet)

urlpatterns = [
    path('', include(vinculos_router.urls))
]