from django.db import models

from materiales.models import Material

class PedidoCliente (models.Model):
	cliente = models.ForeignKey('cliente.Cliente', null = False, blank=True, on_delete=models.CASCADE) 
	productos = models.ManyToManyField(Material)
	comentario = models.CharField(max_length=500)
	entregado = models.BooleanField (default = False)

	def __str__ (self):
		return str(self.id)


class PedidoProveedor (models.Model):
	proveedor = models.ForeignKey('proveedores.Proveedor', null = False, blank = True, on_delete=models.CASCADE)
	productos = models.ManyToManyField(Material)
	comentario = models.CharField(max_length=500)
	entregado = models.BooleanField (default = False) 
