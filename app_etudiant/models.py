from django.db import models
from app_cycle.models import Promotion
from app_cycle.models import Cycle
from django.urls import reverse
from app_User.models import TimeStampedModel
from django.utils import timezone
# Create your models here.

class Etudiant(TimeStampedModel):

    name = models.CharField(max_length=100,null=True, blank=True)
    postnom = models.CharField(max_length=100, null=True, blank=True)
    prenom= models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    genre = models.CharField(max_length=10, choices=[
        ('homme', 'femme'),
    ])
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    promotion = models.ForeignKey(Promotion, null=False, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name











