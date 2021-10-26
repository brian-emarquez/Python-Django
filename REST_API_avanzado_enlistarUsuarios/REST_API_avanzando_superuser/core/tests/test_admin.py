from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.client import Client
from django.urls import reverse

class AdminSiteTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@demo.com', 
            password = 'password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@demo.com',
            password = 'pass123',
            name = 'Test user nombre completo'
        )
        
        def test_users_listed(self):
            """ testeart  a los usuarios ha sido añadiso en la pagina usuario """
            
            url = reverse('admin:core_user_changelist')
            res = self.client.get(url)
            
            self.assertContains(res, self.user.name)
            self.assertContains(res, self.user.email)
            
            
            
        
        
        

