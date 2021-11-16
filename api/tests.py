from django.test import TestCase
from .models import User
# Create your tests here.


class ViewsTestCase(TestCase):
    def setUp(self):
        """Cette méthode se lance avant les tests unitaires"""
        user = User.objects.create(
            nom="uchiha", prenom="sasuke", mail="susano@gmail.com", mdp="sasuke123")
        self.id_user = user.id

    def test_create_user(self):
        """S'inscrire"""

        response = self.client.post('http://localhost:8000/api/create-user/', {
                                    "nom": "uzumaki", "prenom": "naruto", "mail": "kurama@gmail.com", "mdp": "naruto123"})
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        """Se connecter"""

        response = self.client.post(
            'http://localhost:8000/api/login/', {"mail": "susano@gmail.com", "mdp": "sasuke123"})

        self.assertEqual(response.status_code, 200)  # tout va bien
        # verifier le nom d"utilisateur qui s'est connecté
        self.assertEqual(response.data['user']['nom'], "uchiha")

        