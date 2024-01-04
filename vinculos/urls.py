from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from vinculos.api import *

urlpatterns = [
    path('', VinculosAPIList.as_view()),
]