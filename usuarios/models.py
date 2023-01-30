from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_cargo = (('V', 'Vendedor'), ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)
    nome = models.CharField(max_length=40, blank=False, null=False, default=False)
    sobrenome = models.CharField(max_length=40, blank=False, null=False, default=False)
    email = models.CharField(max_length=40, blank=False, null=False, default=False)
    senha = models.CharField(max_length=10, blank=False, null=False, default=False)

