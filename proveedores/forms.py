from django import forms

from proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):

	class Meta:
		model = Proveedor

		fields = [
			'nombre',
			'direccion',
			'telefono',
			'email',
		]

		labels = {
			'nombre': 'Nombre',
			'direccion': 'Dirección',
			'telefono': 'Teléfono',
			'email': 'Email',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
		}