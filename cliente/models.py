from django.db import models
from django.urls import reverse

class Cliente(models.Model):
    nombres=models.CharField(max_length=200)
    apellidos=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    DNI= models.IntegerField()
    edad= models.IntegerField()
    email=models.EmailField()
    telefono=models.IntegerField()
    fechainicio=models.DateField()

    def get_absolute_url(self):
        return reverse('cliente:cliente-detail',kwargs={'pk':self.id})