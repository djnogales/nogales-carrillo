from django.shortcuts import render, redirect
from proveedores.models import Proveedor
from proveedores.forms import ProveedorForm
# Create your views here.

def proveedores_index (request): 
	proveedor = Proveedor.objects.all()
	contexto = {'proveedores': proveedor}
	return render(request, 'proveedores/blank.html', contexto)

def proveedores_view(request): 
	if request.method == 'POST':
		form = ProveedorForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ProveedorForm()

	return render(request, 'proveedores/index.html', {'form':form})