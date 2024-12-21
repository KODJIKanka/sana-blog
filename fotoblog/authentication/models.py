from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    CREATEUR = 'CREATEUR'
    ABONNE = 'ABONNE'

    ROLE_CHOICES = (
        (CREATEUR, 'Créateur'),
        (ABONNE, 'Abonné'),
    )

    profil = models.ImageField(verbose_name = 'Photo de Profil')
    role = models.CharField(max_length = 30, choices = ROLE_CHOICES, verbose_name='Role')
