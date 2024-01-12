from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, cpf, email, password, **extra_fields):
        if not email:
            raise ValueError('The e-mail was not provided')
     
        email = self.normalize_email(email)
        user = self.model(name=name, cpf=cpf, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, name, cpf, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser MUST have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser MUST have is_superuser=True')
        
        return self.create_user(name, cpf, email, password, **extra_fields)