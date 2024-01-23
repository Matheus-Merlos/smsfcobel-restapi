from django.test import TestCase
from django.contrib.auth import get_user_model

class LoginTests(TestCase):
    def get_jwt_acess_token(self):
        
        user_data = {
            'name': "John Doe", 
            'cpf': "13217494903", 
            'email': "normal@user.com", 
            'password': "foo"
        }
        
        User = get_user_model()
        user = User.objects.create_user(**user_data)
        
        response = self.client.post('api/token/', data={"cpf": user_data.get('cpf'), "password": user_data.get('password')})
        return response.get('acess')
    