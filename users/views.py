from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserRegistrationView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
