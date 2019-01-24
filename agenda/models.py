from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    nome = models.CharField(max_length=250)
    data_hora = models.DateTimeField()
    funcionario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

