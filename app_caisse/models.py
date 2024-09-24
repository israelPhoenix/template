from django.db import models
from app_paiestudent.models import paiement

# Create your models here.

class Entrecaisse (models.Model):
    libelle = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)


class Sortiecaisse(models.Model):
    libelle = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    paiEtudiant = models.ForeignKey(paiement, null=False, on_delete=models.CASCADE)

class Operationcaisse(models.Model):
    libellle = models.CharField(max_length=255)
    entree = models.ForeignKey(Entrecaisse, null=False, on_delete=models.CASCADE)
    sortie = models.ForeignKey(Sortiecaisse, null=False, on_delete=models.CASCADE)
