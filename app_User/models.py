from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True



class User(AbstractUser, TimeStampedModel):
    NON_DEFINI = 'non_defini'
    ADMIN = 'ADMIN'
    DOYEN = 'DOYEN'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'

    ROLE_CHOICES = (
        (NON_DEFINI, 'Non défini'),
        (ADMIN, 'Admin'),
        (DOYEN, 'Doyen'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]

    role = models.CharField(default=NON_DEFINI, choices=ROLE_CHOICES, max_length=25, verbose_name="Role")
    profile_photo = models.ImageField(upload_to='profile_photos', null=True, blank=True)
    nationalite = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=65, choices=GENDER_CHOICES, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    rue = models.CharField(max_length=255, null=True, blank=True)
    commune = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Remplacez 'custom_user_set' par un nom unique de votre choix
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        # Remplacez 'custom_user_permissions_set' par un nom unique de votre choix
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    def get_redirect_url(self):
        """
        Renvoie l'URL de redirection en fonction du rôle de l'utilisateur.
        """
        role_map = {
            self.ADMIN: reverse('dashboard-admin'),
            self.DOYEN: reverse('dashboard-doyen'),
            self.TEACHER: reverse('dashboard-doyen'),
            self.STUDENT: reverse('dashboard-doyen'),
        }
        return role_map.get(self.role, reverse('login'))

    """    @property
    def has_company(self):

        from app_entreprise.models import Compagnie
        return Compagnie.objects.filter(admin=self).exists() """

