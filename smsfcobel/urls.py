from django.contrib import admin
from rest_framework.routers import SimpleRouter
from users import views
from django.urls import path, include
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView, TokenVerifyView
from users.views import CustomTokenObtainPairView

users_router = SimpleRouter(trailing_slash=True)

users_router.register('api/permissions', views.PermissionsViewSet, basename='permissions')
users_router.register('api/users/all', views.AllUsersViewSet)
users_router.register('api/users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vinculos/api/', include('vinculos.urls')),
    
    path('api/register/', views.UserRegistrationView.as_view()),
    path('api/change-password/', views.ChangePasswordView.as_view()),
    
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns.extend(users_router.urls)
