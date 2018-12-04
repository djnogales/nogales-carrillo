from django.db import models

# Create your models here.

class Factura (models.Model):
	envio = models.ForeignKey ('envios.EnvioCliente', null = False, blank = True, on_delete = models.CASCADE)
	cliente = models.ForeignKey ('cliente.Cliente', null = False, blank = True, on_delete = models.CASCADE)
	importe = models.FloatField()
	estado = models.CharField(max_length = 30)
	fecha = models.DateField()
	pagada = models.BooleanField()

