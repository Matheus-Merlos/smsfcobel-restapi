from rest_framework import serializers
from vinculos.validators import *
from vinculos.models import *

class FuncionarioSerializer(serializers.ModelSerializer):
    emissao_rg = serializers.DateField(format='%d/%m/%Y')
    data_nascimento = serializers.DateField(format='%d/%m/%Y')
    sexo_codigo = serializers.PrimaryKeyRelatedField(queryset=Sexo.objects.all(), source='sexo', write_only=True, required=True)
    sexo = serializers.StringRelatedField(source='sexo.descricao', read_only=True)
    class Meta:
        model = Funcionario
        fields = ['nome', 'sexo_codigo', 'sexo', 'cpf', 'rg', 'emissao_rg', 'cns', 'email', 'nome_mae', 'nome_pai', 'data_nascimento', 'operador', 'profissional']
        
    def validate(self, attrs):
        super_validate = super().validate(attrs)
        FuncionarioValidator(data=attrs)
        return super_validate

class VinculoSerializer(serializers.ModelSerializer):
    tipo_vinculo = serializers.StringRelatedField(source='tipo_vinculo.descricao')
    nome = serializers.StringRelatedField(source='funcionario.nome')
    cpf = serializers.StringRelatedField(source='funcionario.cpf')
    rg = serializers.StringRelatedField(source='funcionario.rg')
    emissao_rg = serializers.DateField(format='%d/%m/%Y', source='funcionario.emissao_rg')
    local = serializers.StringRelatedField(source='local.descricao')
    email = serializers.StringRelatedField(source='funcionario.email')
    nome_mae = serializers.StringRelatedField(source='funcionario.nome_mae')
    nome_pai = serializers.StringRelatedField(source='funcionario.nome_pai')
    cns = serializers.StringRelatedField(source='funcionario.cns')
    funcao = serializers.StringRelatedField(source='funcao.descricao')

    operador = serializers.StringRelatedField(source='funcionario.operador')
    profissional = serializers.StringRelatedField(source='funcionario.profissional')
    
    data_criacao = serializers.DateField(format='%d/%m/%Y')
    data_entrada = serializers.DateField(format='%d/%m/%Y')
    tipo = serializers.DateField(format='%d/%m/%Y', source='tipo.descricao')
    
    class Meta:
        model = Vinculo
        fields = ['tipo_vinculo', 'nome', 'cpf', 'rg', 'emissao_rg', 'local', 'email', 'nome_mae', 'nome_pai', 'cns', 'funcao', 'operador', 'profissional', 'data_criacao', 'data_entrada', 'tipo']

    
