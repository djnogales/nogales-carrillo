from django import forms
from envios.models import EnvioCliente

class EnvioClienteForm(forms.ModelForm):
	class Meta:
		model = EnvioCliente

		fields = [
			'pedido',
			'transportista',
			'vehiculo',
			'direccionEnvio',
			'comentario',
			'fecha',
		]

		labels = {
			'pedido': 'Pedido',
			'transportista': 'Transportista',
			'vehiculo': 'Vehículo',
			'direccionEnvio': 'Dirección de envío',
			'comentario': 'Comentario',
			'fecha': 'Fecha',
		}

		widgets = {
			'pedido': forms.Select(attrs={'class':'form-control'}),
			'transportista': forms.Select(attrs={'class':'form-control'}),
			'vehiculo': forms.Select(attrs={'class':'form-control'}),
			'direccionEnvio': forms.TextInput(attrs={'class':'form-control'}),
			'comentario': forms.TextInput(attrs={'class':'form-control'}),
			'fecha': forms.DateInput(attrs={'class':'form-control'}),
		}