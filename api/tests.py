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
 
    def test_update_user(self):
        """Met à jour l'utilisateur"""

        response = self.client.put(
            'http://localhost:8000/api/user/' + str(self.id_user) + '/', {
                "nom": "God",
                "prenom": "Madara",
                "mdp": "hashirama123",
                "mail": "susano@gmail.com"
            }, content_type="application/json")

        self.assertEqual(response.status_code, 200)  # tout va bien

        response = self.client.get(
            'http://localhost:8000/api/user/' + str(self.id_user) + '/')

        # verifier si la mise à jour a bien été effectué
        self.assertEqual(response.data['nom'], "God")
        self.assertEqual(response.data['prenom'], "Madara")

    def test_delete_user(self):
        """Supprimer un utilisateur"""

        response = self.client.delete(
            'http://localhost:8000/api/user/' + str(self.id_user) + '/')

        self.assertEqual(response.status_code, 204)  # tout va bien

        response = self.client.get(
            'http://localhost:8000/api/user/' + str(self.id_user) + '/')
        self.assertEqual(response.status_code, 404)

    def test_add_to_watchlist(self):
        """Ajouter un Anime à sa WatchList"""

        response = self.client.post(
            'http://127.0.0.1:8000/api/watchlist/', {"userId": self.id_user, "tmdbId": 6949, "name": "Tokyo Revengers", "imageUrl": "https://tokyo.png"})

        # tout va bien, l'anime de l'utilisateur a été ajouté dans sa watchlist
        self.assertEqual(response.status_code, 201)
