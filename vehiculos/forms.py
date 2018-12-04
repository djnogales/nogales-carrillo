from django import forms

from vehiculos.models import Vehiculo

class VehiculoForm(forms.ModelForm):

	class Meta:
		model = Vehiculo

		fields = [
			'matricula',
			'tipo',
			'fechaMatriculacion',
			'kms',
		]

		labels = {
			'matricula': 'Matricula',
			'tipo': 'Tipo',
			'fechaMatriculacion': 'Fecha de matriculación',
			'kms': 'Kilómetros',
		}

		widgets = {
			'matricula': forms.TextInput(attrs={'class':'form-control'}),
			'tipo': forms.TextInput(attrs={'class':'form-control'}),
			'fechaMatriculacion': forms.DateInput(attrs={'class':'form-control'}),
			'kms': forms.TextInput(attrs={'class':'form-control'}),
		}