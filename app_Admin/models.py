from django.db import models

# Create your models here.

class Personel(models.Model):
    name = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    etat_civil = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)



