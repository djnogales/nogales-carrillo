from django.db import models

# Create your models here.

class Proveedor (models.Model):
	nombre = models.CharField (max_length = 200)
	direccion = models.CharField (max_length = 200)
	telefono = models.IntegerField()
	email = models.EmailField()

	def __str__ (self):
		return self.nombre
