from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    longitud = models.FloatField(null=True)
    latitud = models.FloatField(null=True)
    estadogeo = models.BooleanField(default=False) #que tipo de field? boolean

    class Meta:
        ordering = ('nombre', )

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
