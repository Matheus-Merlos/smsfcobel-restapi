from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser, Permissions
from users.serializers import CustomUserSerializer, PermissionsSerializer, AllUsersSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

class UserRegistrationView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class PermissionsViewSet(ReadOnlyModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class AllUsersViewSet(ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AllUsersSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    

class ChangePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        cpf = request.data.get('cpf')
        new_password = request.data.get('password')
        
        # Verifica se há um usuário com o email e o cpf indicados
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email, cpf=cpf)
        except user_model.DoesNotExist:
            return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Define e salva a nova senha
        user.set_password(new_password)
        user.save()
        
        return Response({'message': 'Senha alterada com sucesso'}, status=status.HTTP_200_OK)


