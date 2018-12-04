from django import forms

from cliente.models import Cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'nombre',
			'direccion',
			'telefono',
			'dni',
		]

		labels = {
			'nombre': 'Nombre',
			'direccion': 'Dirección',
			'telefono': 'Teléfono',
			'dni': 'DNI',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'dni': forms.TextInput(attrs={'class':'form-control'}),
		}