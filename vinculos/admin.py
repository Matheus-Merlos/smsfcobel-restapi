from django.contrib import admin
from vinculos import models

# Register your models here.
@admin.register(models.Sexo)
class SexoAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)
    
    
@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)


@admin.register(models.StatusRH)
class StatusRHAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)
    
    
@admin.register(models.Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)


@admin.register(models.Local)
class LocalAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)


@admin.register(models.Tipo)
class TipoAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)


@admin.register(models.TipoVinculo)
class TipoVinculoAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)


@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'nome', 'get_sexo_descricao', 'cpf', 'cns', 'rg', 'emissao_rg', 'email', 'nome_mae', 'nome_pai', 'data_nascimento', 'operador', 'profissional')
    
    def get_sexo_descricao(self, obj):
        return obj.sexo.descricao

@admin.register(models.Vinculo)
class VinculoAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'funcionario_nome', 'carga_horaria', 'data_entrada', 'data_saida', 'data_criacao', 'data_edicao')
    list_editable = ('carga_horaria', 'data_entrada', 'data_saida')
    
    def funcionario_nome(self, obj):
        return obj.funcionario.nome