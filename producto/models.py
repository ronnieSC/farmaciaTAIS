from django.db import models
from django.urls import reverse
from proveedor.models import Proveedor

class Producto(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=200)
	proveedor=models.CharField(max_length=100)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	precio= models.FloatField()
	cantidad= models.IntegerField()
	oferta=models.BooleanField()
	imagen=models.ImageField(upload_to='static/images/',null=True) 

	def get_absolute_url(self):
		return reverse('producto:Producto_edit',kwargs={'myID':self.id})