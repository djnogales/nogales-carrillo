from django.db import models

# Create your models here.

class Transportista (models.Model):
	nombre = models.CharField(max_length = 200)
	tipo = models.CharField (max_length = 30)
	dni = models.CharField (max_length = 9)
	sueldo = models.FloatField()
	planta = models.CharField(max_length = 15)

	def __str__(self):
		return self.nombre