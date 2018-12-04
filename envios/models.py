from django.db import models

# Create your models here.

class EnvioCliente (models.Model):
	pedido = models.ForeignKey ('pedidos.PedidoCliente', null = False, blank = True, on_delete = models.CASCADE)
	transportista = models.ForeignKey ('transportistas.Transportista', null = False, blank = True, on_delete = models.CASCADE)
	vehiculo = models.ForeignKey ('vehiculos.Vehiculo', null = False, blank = True, on_delete = models.CASCADE)
	direccionEnvio = models.CharField(max_length = 200)
	comentario = models.CharField (max_length = 500)
	fecha = models.DateField()