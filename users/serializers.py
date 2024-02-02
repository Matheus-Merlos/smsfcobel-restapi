from rest_framework import serializers
from users.models import CustomUser, Permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'cpf', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            name=validated_data['name'],
            cpf=validated_data['cpf'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Adicione campos adicionais que você deseja incluir no retorno do token
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = self.user.name
        data['cpf'] = self.user.cpf
        data['permissions'] = [permission.descricao for permission in Permissions.objects.all().filter(customuser__cpf=self.user.cpf)]
        return data    