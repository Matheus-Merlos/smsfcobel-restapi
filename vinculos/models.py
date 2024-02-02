from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Model

# Create your models here.
class Sexo(Model):
    """
    Model para conter os tipos de sexo
    """
    descricao = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.descricao
    
    
class Status(Model):
    """Model que contém o status do vínculo, isto é, se ele foi criado ou não, é utilizado para o CNES e IDS"""
    descricao = models.CharField(max_length=31)

    def __str__(self) -> str:
        return self.descricao

class StatusRH(Model):
    """Model que contém o status do vínculo no RH, se já foi criado ou não."""
    descricao = models.CharField(max_length=31)

    def __str__(self) -> str:
        return self.descricao


class Funcao(Model):
    """Model que contém as funções dos vínculos, isto é, se ele é um enfermeiro, um médico, etc."""
    descricao = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.descricao
    
    
class Local(Model):
    """Model que contém o local de trabalho do vínculo, com o CSCN, UPA, Etc."""
    descricao = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.descricao


class Tipo(Model):
    """Model que contém o tipo do vínculo, se é estágiário, estatutário, PSS, etc."""
    descricao = models.CharField(max_length=31)

    def __str__(self) -> str:
        return self.descricao
    
class TipoVinculo(Model):
    """Model que contém o tipo do vínculo, ou seja, se é novo, se é pra adicionar local, transferir local ou remover de local."""
    descricao = models.CharField(max_length=63)
    
    def __str__(self) -> str:
        return self.descricao

class Funcionario(Model):
    """Model que contém as informações do funcionário"""
    nome = models.CharField(max_length=255, unique=True)
    
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT, null=False, blank=False)
    
    cpf = models.CharField(unique=True, max_length=11)
    cns = models.IntegerField(unique=True)
    rg = models.IntegerField(unique=True)
    emissao_rg = models.DateField()
    email = models.EmailField()
    crm = models.CharField(max_length=31, blank=True, null=True)
    nome_mae = models.CharField(max_length=255)
    nome_pai = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    operador = models.IntegerField(null=True, blank=True, default=None)
    profissional = models.IntegerField(null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return self.nome
    
class Vinculo(Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=False, default=0)
    
    carga_horaria = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True, blank=True)
    data_edicao = models.DateField(auto_now=True)
    
    status_cnes = models.ForeignKey(Status, on_delete=models.PROTECT, null=False, related_name='status_cnes', default=1)
    status_ids = models.ForeignKey(Status, on_delete=models.PROTECT, null=False, related_name='status_ids', default=1)
    status_rh = models.ForeignKey(StatusRH, on_delete=models.PROTECT, null=False, default=1)
    funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT, null=False)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, null=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, null=False)
    tipo_vinculo = models.ForeignKey(TipoVinculo, on_delete=models.PROTECT, null=False)
    
