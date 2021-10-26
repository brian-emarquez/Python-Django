from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    
    def test_create_user_with_email_succesful(self):
        """Porbar cerando un nvo usuario con un Email email correctamente"""
        
        email = 'test@demo.com'
        password = 'Testpass123'
        
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
        
    """ normalisar """
    def test_new_user_email_normalized(self):
        """Testea email para nuero usuario normalizado"""
        
        email = 'test@DEMO.com'
        user = get_user_model().objects.create_user(email, 'Testpass123')
        
        self.assertEqual(user.email, email.lower())
        
    def test_new_user_invalid_email(self):
        """ nuevo usuario email invalido """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Testpass123')
            
        
        
        

        
        
        
    
            
        