from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length = 200)
	direccion = models.CharField(max_length = 200)
	telefono = models.IntegerField()
	dni = models.CharField(max_length = 9)

	def __str__(self):
		return self.nombre

