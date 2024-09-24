from django.db import models
from app_cycle.models import Promotion
from app_cycle.models import Cycle
# Create your models here.

class Inscription(models.Model):

    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_creation = models.DateTimeField(auto_now_add=True)
    promotion = models.ForeignKey(Promotion, null=False, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name











