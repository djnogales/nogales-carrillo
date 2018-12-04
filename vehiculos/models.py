from django.db import models

# Create your models here.

class Vehiculo (models.Model):
	matricula = models.CharField (max_length = 7)
	tipo = models.CharField (max_length = 20)
	fechaMatriculacion = models.DateField()
	kms = models.IntegerField()

	def __str__ (self):
		return self.matricula