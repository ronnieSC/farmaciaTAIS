from django.db import models
from django.urls import reverse
from cliente.models import Cliente
from django.contrib.auth.models import User

class Venta(models.Model):
	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
	vendedor=models.ForeignKey(User, on_delete=models.CASCADE)
	detalles=models.TextField()
	total=models.IntegerField()
	fecha= models.DateTimeField()

	def get_absolute_url(self):
		return reverse('venta:Venta_details',kwargs={'myID':self.id})