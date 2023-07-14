from django.db import models

# Create your models here.


class Paises(models.Model):
    nombre = models.CharField(max_length=100)
    colores_bandera = models.CharField(max_length=100)
    fundacion = models.DateField()
    dia_nacional = models.DateField()
    baile_nacional = models.CharField(max_length=100)
    animal_nacional = models.CharField(max_length=100)
