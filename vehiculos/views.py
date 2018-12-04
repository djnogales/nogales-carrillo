from django.shortcuts import render, redirect
from vehiculos.models import Vehiculo
from vehiculos.forms import VehiculoForm
# Create your views here.

def vehiculos_index (request): 
	vehiculo = Vehiculo.objects.all()
	contexto = {'vehiculos': vehiculo}
	return render(request, 'vehiculos/blank.html', contexto)

def vehiculos_view(request): 
	if request.method == 'POST':
		form = VehiculoForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = VehiculoForm()

	return render(request, 'vehiculos/index.html', {'form':form})