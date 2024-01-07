from rest_framework.routers import SimpleRouter
from django.urls import path, include
from vinculos import api

app_name = 'vinculos'

vinculos_router = SimpleRouter(trailing_slash=True)
vinculos_router.register('funcionarios', api.FuncionarioViewSet, basename='funcionarios')
vinculos_router.register('', api.VinculosViewSet)

urlpatterns = [
    path('', include(vinculos_router.urls))
]