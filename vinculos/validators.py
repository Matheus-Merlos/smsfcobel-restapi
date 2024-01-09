from rest_framework.serializers import ValidationError
from datetime import datetime
from abc import ABC, abstractmethod
from django.shortcuts import get_object_or_404
from vinculos import models
import re

class Validator(ABC):
    def __init__(self, data: dict, error_class: type[Exception]=ValidationError):
        self.data = data
        self.ErrorClass = error_class
        self.validate(data)
    
    @abstractmethod
    def validate(self, data): ...

class FuncionarioValidator:
    def __init__(self, data: dict, ErrorClass: type[Exception]=ValidationError):
        self.data = data
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.validate(data)
    
    def validate(self, *args):
        self.validate_field('cpf', 10)
        self.validate_field('rg', 8)
        self.validate_field('cns', 14)
    
    def validate_field(self, field_name: str, desired_lenght: int) -> None:
        field = str(self.data.get(field_name))
        if len(field) != desired_lenght:
            raise self.ErrorClass(f'This {field_name.upper()} is not valid!')
    