from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from vinculos.api import *

urlpatterns = [
    path('', VinculosAPIList.as_view()),
    path('funcionarios/', FuncionarioAPIList.as_view()),
    path('funcionarios/<int:pk>', FuncionarioAPI.as_view())
]