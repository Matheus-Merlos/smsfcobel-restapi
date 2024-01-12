from rest_framework import serializers
from users.models import CustomUser

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
        