from django.db import models

# Create your models here.
class Cycle(models.Model):
    nom = models.CharField(max_length=100)
class Filiere(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="service_images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cycle = models.ForeignKey(Cycle, null=False, on_delete=models.CASCADE)

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    cycle = models.ForeignKey(Cycle, null=False, on_delete=models.CASCADE)



