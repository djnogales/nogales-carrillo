from django.db import models

# Create your models here.

class Material (models.Model):
	nombre = models.CharField (max_length = 200)
	tipo = models.CharField (max_length = 50)
	caracteristicas = models.CharField (max_length = 300)
	cantidad = models.IntegerField ()

	def __str__(self):
		return self.nombre
