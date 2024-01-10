from rest_framework.serializers import ValidationError
from datetime import date
from abc import ABC, abstractmethod

class Validator(ABC):
    def __init__(self, data: dict, error_class: type[Exception]=ValidationError):
        self.data = data
        self.ErrorClass = error_class
        self.errors = {}
        self.validate(data)
    
    @abstractmethod
    def validate(self, data): 
        if self.errors:
            raise self.ErrorClass(self.errors)

class FuncionarioValidator(Validator):
    def validate(self, data):
        self.validate_name('nome')
        self.validate_name('nome_mae')
        self.validate_name('nome_pai')
        
        self.validate_number_field('cpf', 11)
        self.validate_number_field('cns', 15)
        
        self.validate_rg()
        
        data_nascimento = self.data.get('data_nascimento')
        data_emissao_rg = self.data.get('emissao_rg')
        
        assert isinstance(data_nascimento, date)
        assert isinstance(data_emissao_rg, date)
        
        if data_emissao_rg > data_nascimento:
            self.errors['data_nascimento'] = 'The ID issuance date is greater than the date of birth'
            self.errors['emissao_rg'] = 'The ID issuance date is greater than the date of birth'
        
        super().validate(data)
    
    def validate_name(self, name_field_name: str) -> None:
        name = self.data.get(name_field_name)
        name_as_list = name.split(' ')
        if len(name_as_list) < 2:
            self.errors[name_field_name] = 'This name is not valid'
    
    def validate_number_field(self, number_field_name: str, desired_lenght: int) -> None:
        number = str(self.data.get(number_field_name))
        if len(number) != desired_lenght:
            self.errors[number_field_name] = f'This {number_field_name} is not valid'
    
    def validate_rg(self):
        rg = str(self.data.get('rg'))
        if len(rg) > 10 or len(rg) < 6:
            self.errors['rg'] = 'The provided RG is not valid'

class VinculoValidator(Validator): 
    def validate(self, data):
        
        data_entrada = self.data.get('data_entrada')
        data_saida = self.data.get('data_saida')
        
        assert isinstance(data_entrada, date)
        assert isinstance(data_saida, date)
        
        if data_entrada > data_saida:
            self.errors['data_entrada'] = 'The departure date is greater than the arrival date'
            self.errors['data_saida'] = 'The departure date is greater than the arrival date'
        
        super().validate(data)
        