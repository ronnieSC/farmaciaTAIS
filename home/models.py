from django.db import models

class Sticky(models.Model):
	titulo=models.CharField(max_length=300)
	subtitulo=models.CharField(max_length=300)
	descripcion=models.TextField()
	color=models.CharField(max_length=300,blank=True)

class Testimonial(models.Model):
	nombre=models.CharField(max_length=300)
	descripcion=models.TextField()
	imagen=models.ImageField(upload_to='static/images/',null=True) 


