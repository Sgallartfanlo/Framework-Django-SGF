from django.db import models

class Titol(models.Model):
    nom = models.CharField(max_length=200)
    any = models.IntegerField()

    def __str__(self):
        return f"{self.nom} ({self.any})"

class Jugador(models.Model):
    nom = models.CharField(max_length=200)
    posicio = models.CharField(max_length=100)
    nacionalitat = models.CharField(max_length=100)
    titols = models.ManyToManyField(Titol, related_name="jugadors")

    def __str__(self):
        return self.nom
