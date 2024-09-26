from django.db import models

# Create your models here.
class Cycle(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Promotion(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    cycle = models.ForeignKey(Cycle, null=False, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
class Filiere(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promotions = models.ForeignKey(Promotion, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




