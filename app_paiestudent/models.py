from django.db import models
# Create your models here.
from app_Inscription.models import Inscription
class paiement(models.Model):
    info_etudiant = models.ForeignKey(Inscription, null=False, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    motif_paiement = models.CharField(max_length=100)