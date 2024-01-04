from rest_framework.serializers import ValidationError
import re

class FuncionarioValidator:
    def __init__(self, data: dict, ErrorClass: Exception=None):
        self.data = data
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.validate(data)
    
    def validate(self, *args):
        self.validate_field('cpf', 10)
        self.validate_field('rg', 8)
        self.validate_field('cns', 14)
        self.validate_gender()
    
    def validate_field(self, field_name: str, desired_lenght: int) -> None:
        field = str(self.data.get(field_name))
        if len(field) != desired_lenght:
            raise self.ErrorClass(f'This {field_name.upper()} is not valid!')
    
    def validate_gender(self):
        genders = ['MASCULINO', 'FEMININO']
        gender = str(self.data.get('sexo'))
        print(gender)
        if gender not in genders:
            raise self.ErrorClass('This gender is not valid!')