from django.db import models
from app_Inscription.models import Inscription

# Create your models here.

class etudiant(models.Model):

    info_etudiant = models.ForeignKey(Inscription, null=False, on_delete=models.CASCADE)
