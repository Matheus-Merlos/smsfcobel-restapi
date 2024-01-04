from rest_framework import serializers
from vinculos.models import *

class VinculoSerializer(serializers.ModelSerializer):
    tipo_vinculo = serializers.StringRelatedField(source='tipo_vinculo.descricao')
    nome = serializers.StringRelatedField(source='funcionario.nome')
    cpf = serializers.SerializerMethodField()
    rg = serializers.SerializerMethodField()
    emissao_rg = serializers.DateField(format='%d/%m/%Y', source='funcionario.emissao_rg')
    local = serializers.StringRelatedField(source='local.descricao')
    email = serializers.StringRelatedField(source='funcionario.email')
    nome_mae = serializers.StringRelatedField(source='funcionario.nome_mae')
    nome_pai = serializers.StringRelatedField(source='funcionario.nome_pai')
    cns = serializers.SerializerMethodField()
    funcao = serializers.StringRelatedField(source='funcao.descricao')
    
    class Meta:
        model = Vinculo
        fields = ['tipo_vinculo', 'nome', 'cpf', 'rg', 'emissao_rg', 'local', 'email', 'nome_mae', 'nome_pai', 'cns', 'funcao']
        
    def get_cpf(self, obj: Vinculo) -> str:
        cpf = str(obj.funcionario.cpf)
        cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return cpf
    
    def get_rg(self, obj: Vinculo) -> str:
        rg = str(obj.funcionario.rg)
        rg = f'{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}'
        return rg
    
    def get_cns(self, obj: Vinculo) -> str:
        cns = str(obj.funcionario.cns)
        cns = f'{cns[:4]}.{cns[4:8]}.{cns[8:12]}.{cns[12:]}'
        return cns
