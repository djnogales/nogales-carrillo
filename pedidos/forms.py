from django import forms
from pedidos.models import PedidoCliente, PedidoProveedor

class PedidoClienteForm(forms.ModelForm):
	class Meta:
		model = PedidoCliente

		fields = [
			'cliente',
			'productos',
			'comentario',
			'entregado',
		]

		labels = {
			'cliente': 'Cliente',
			'productos': 'Productos',
			'comentario': 'Comentario',
			'entregado': 'Entregado',
		}

		widgets = {
			'cliente': forms.Select(attrs={'class':'form-control'}),
			'productos': forms.CheckboxSelectMultiple(),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'entregado': forms.CheckboxInput(attrs={'class':'form-control'}),
		}

class PedidoProveedorForm(forms.ModelForm):
	class Meta:
		model = PedidoProveedor

		fields = [
			'proveedor',
			'productos',
			'comentario',
			'entregado',
		]

		labels = {
			'proveedor': 'Proveedor',
			'productos': 'Productos',
			'comentario': 'Comentario',
			'entregado': 'Entregado',
		}

		widgets = {
			'proveedor': forms.Select(attrs={'class':'form-control'}),
			'productos': forms.CheckboxSelectMultiple(),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'entregado': forms.CheckboxInput(attrs={'class':'form-control'}),
		}
