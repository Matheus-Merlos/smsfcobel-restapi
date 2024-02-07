from rest_framework import serializers
from users.models import CustomUser, Permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'cpf', 'email', 'password', 'permissions']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions', [])  # Extrai as permissões da entrada
        user = CustomUser.objects.create_user(**validated_data)

        user.permissions.add(*permissions_data)

        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['user'] = self.user.name
        data['cpf'] = self.user.cpf
        data['email'] = self.user.email
        permissions = [permission.descricao for permission in Permissions.objects.all().filter(customuser__cpf=self.user.cpf)]
        data['permissions'] = permissions
        return data    

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ['id', 'descricao']


class AllUsersSerializer(serializers.ModelSerializer):
    permissions = PermissionsSerializer(many=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'cpf', 'email', 'permissions']