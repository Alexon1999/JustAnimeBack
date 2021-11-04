from django.db import models

# Create your models here.


class Content(models.Model):
    name = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=2048)
    tmdb_id = models.IntegerField()  # cet id viendra de TMDB Api

    def __str__(self):
        return self.name


# TODO: JWT Token Authentication
# https://www.youtube.com/watch?v=AfYfvjP1hK8&t=1670s
class User(models.Model):
    nom = models.CharField(max_length=31)
    prenom = models.CharField(max_length=31)
    mail = models.CharField(max_length=31, unique=True)
    mdp = models.CharField(max_length=31)
    watch_list = models.ManyToManyField(Content, blank=True)

    def __str__(self):
        return self.nom + " " + self.prenom
