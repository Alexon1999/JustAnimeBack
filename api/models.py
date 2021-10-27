from django.db import models

# Create your models here.


class User(models.Model):
    nom = models.CharField(max_length=31)
    prenom = models.CharField(max_length=31)
    mail = models.CharField(max_length=31, unique=True)
    mdp = models.CharField(max_length=31)

    def str(self):
        return self.nom + " " + self.prenom
