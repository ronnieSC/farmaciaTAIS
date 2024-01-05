from django.db import models
from django.urls import reverse

class Proveedor(models.Model):
    razonsocial=models.CharField(max_length=300)
    direccion=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    telefono=models.IntegerField()
    representante=models.CharField(max_length=300)
    fechacontratacion=models.DateField()

    def __str__(self):
        return self.razonsocial
    def __unicode__(self):
        return self.razonsocial

    def get_absolute_url(self):
        return reverse('proveedor:Proveedor_edit',kwargs={'myID':self.id})