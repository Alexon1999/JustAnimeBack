# Objectif
- Une plateforme de streaming qui permettra de donner accès aux catalogues Animes et avoir la possibilité d'obtenir une watchlist.

# Fonctionnalités de l'API
- Cette API permettra d'enregistrer les données d'un utilisateur.
- Permettre la gestion de données des utilisateurs en tant qu'admin.
- Créer un watchlist pour des utilisateurs.
- Disponibilité d'une documentation avec OpenAPI & Swagger.
- Test de l'API avec Postman.
- Tests unitaires dans api/tests.py.
- Cette API intéragit avec un front développé sous Flutter (https://github.com/ghilesalt/mobile-mugiwara-s.git).
    - Utilisation d'une API externe pour récupérer les données sur les Animes.

## Pour Lancer
- python -m venv env
- env/scripts/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- python manage.py test (lancer le test)

## La documentation de cette API
- [Voir la doc](https://documenter.getpostman.com/view/11867175/UVC2GU8E)
