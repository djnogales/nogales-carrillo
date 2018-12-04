from django import forms

from transportistas.models import Transportista

class TransportistaForm(forms.ModelForm):

	class Meta:
		model = Transportista

		fields = [
			'nombre',
			'tipo',
			'dni',
			'sueldo',
			'planta',
		]

		labels = {
			'nombre': 'Nombre',
			'tipo': 'Tipo',
			'dni': 'DNI',
			'sueldo': 'Sueldo',
			'planta': 'Planta',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'tipo': forms.TextInput(attrs={'class':'form-control'}),
			'dni': forms.TextInput(attrs={'class':'form-control'}),
			'sueldo': forms.TextInput(attrs={'class':'form-control'}),
			'planta': forms.TextInput(attrs= {'class': 'form-control'}),
		}