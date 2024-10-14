from django.db import models
from app_paiestudent.models import paiement
from app_User.models import TimeStampedModel

# Create your models here.

class Entrecaisse (TimeStampedModel):
    libelle = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.libelle

class Sortiecaisse(TimeStampedModel):
    libelle = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.libelle

