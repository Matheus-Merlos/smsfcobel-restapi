from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from users.managers import UserManager
from django.db.models import Model
from django.db import models

class Permissions(Model):
    descricao = models.CharField(max_length=31)

    def __str__(self) -> str:
        return self.descricao

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    permissions = models.ManyToManyField(Permissions)
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['name', 'email']
    
    objects = UserManager()
    
    def __str__(self) -> str:
        return self.name

