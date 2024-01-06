from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from vinculos.api import *

urlpatterns = [
    path('', VinculosViewSet.as_view({
        'get': 'list'
        })),
    path('funcionarios/', FuncionarioViewSet.as_view({
        'get': 'list',
        'post': 'create'
        })),
    path('funcionarios/<int:pk>', FuncionarioViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    }))
]