from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class VinculosTests(TestCase):
    def test_vinculo_api_list_returns_status_code_200(self):
        api_url = reverse('vinculos:vinculos-pendentes-list')
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)
        
        