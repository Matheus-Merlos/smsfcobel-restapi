from rest_framework import serializers
from vinculos import validators
from vinculos.models import *

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['id', 'descricao']
        
class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = ['id', 'descricao']

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'descricao']
        
class TipoVinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVinculo
        fields = ['id', 'descricao']
        
class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = ['id', 'descricao']

class FuncionarioSerializer(serializers.ModelSerializer):
    emissao_rg = serializers.DateField(format='%d/%m/%Y')
    data_nascimento = serializers.DateField(format='%d/%m/%Y')
    sexo_codigo = serializers.PrimaryKeyRelatedField(queryset=Sexo.objects.all(), source='sexo', write_only=True, required=True)
    sexo = serializers.StringRelatedField(source='sexo.descricao', read_only=True)
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'crm', 'sexo_codigo', 'sexo', 'cpf', 'rg', 'emissao_rg', 'cns', 'email', 'nome_mae', 'nome_pai', 'data_nascimento', 'operador', 'profissional']
        
    def validate(self, attrs):
        #validators.FuncionarioValidator(attrs)
        return super().validate(attrs)
        

class VinculoSerializer(serializers.ModelSerializer):
    
    data_entrada = serializers.DateField(format='%d/%m/%Y')
    data_saida = serializers.DateField(format='%d/%m/%Y')
    
    funcionario_codigo = serializers.PrimaryKeyRelatedField(queryset=Funcionario.objects.all(), source='funcionario', write_only=True, required=True)
    funcionario = serializers.StringRelatedField(source='funcionario.nome', read_only=True)
    
    funcao_codigo = serializers.PrimaryKeyRelatedField(queryset=Funcao.objects.all(), source='funcao', write_only=True, required=True)
    funcao = serializers.StringRelatedField(source='funcao.descricao', read_only=True)

    local_codigo = serializers.PrimaryKeyRelatedField(queryset=Local.objects.all(), source='local', write_only=True, required=True)
    local = serializers.StringRelatedField(source='local.descricao', read_only=True)
    
    tipo_codigo = serializers.PrimaryKeyRelatedField(queryset=Tipo.objects.all(), source='tipo', write_only=True, required=True)
    tipo = serializers.StringRelatedField(source='tipo.descricao', read_only=True)
    
    tipo_vinculo_codigo = serializers.PrimaryKeyRelatedField(queryset=TipoVinculo.objects.all(), source='tipo_vinculo', write_only=True, required=True)
    tipo_vinculo = serializers.StringRelatedField(source='tipo_vinculo.descricao', read_only=True)
    
    status_ids_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), write_only=True, default=1)

    
    class Meta:
        model = Vinculo
        fields = ['id', 'funcionario_codigo', 'funcionario', 'carga_horaria', 'data_entrada', 'data_saida', 'funcao_codigo', 'funcao', 'local_codigo', 'local', 'tipo_codigo', 'tipo', 'tipo_vinculo_codigo', 'tipo_vinculo', 'status_ids_id']
    
    def validate(self, attrs):
        #validators.VinculoValidator(attrs)
        return super().validate(attrs)
    

class VinculosPendentesSerializer(serializers.ModelSerializer):
    profissional_id = serializers.StringRelatedField(source='funcionario.id')
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
    sexo = serializers.StringRelatedField(source='funcionario.sexo.descricao')

    operador = serializers.StringRelatedField(source='funcionario.operador')
    profissional = serializers.StringRelatedField(source='funcionario.profissional')
    
    data_criacao = serializers.DateField(format='%d/%m/%Y')
    data_entrada = serializers.DateField(format='%d/%m/%Y')
    data_nascimento = serializers.DateField(format='%d/%m/%Y', source='funcionario.data_nascimento')
    tipo = serializers.DateField(format='%d/%m/%Y', source='tipo.descricao')
    
    crm = serializers.StringRelatedField(source='funcionario.crm')
    
    status_ids = serializers.StringRelatedField(source='status_ids.descricao')
    status_cnes = serializers.StringRelatedField(source='status_cnes.descricao')
    status_rh = serializers.StringRelatedField(source='status_rh.descricao')
    
    class Meta:
        model = Vinculo
        fields = ['id', 'profissional_id', 'tipo_vinculo', 'nome', 'cpf', 'rg', 'emissao_rg', 'local', 'email', 'sexo', 'nome_mae', 'nome_pai', 'cns', 'funcao', 'operador', 'profissional', 'data_criacao', 'data_entrada', 'data_nascimento', 'tipo', 'crm', 'carga_horaria', 'status_ids', 'status_cnes', 'status_rh']

