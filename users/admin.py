from django.contrib import admin
from users import models

@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'cpf', 'email', )
    list_editable = ('name', 'cpf', 'email', )
    

@admin.register(models.Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'descricao')
    list_editable = ('descricao',)
