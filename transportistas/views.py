from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from transportistas.models import Transportista
from transportistas.forms import TransportistaForm
# Create your views here.

def transportistas_index (request): 
	transportista = Transportista.objects.all()
	contexto = {'transportistas': transportista}
	return render(request, 'transportistas/blank.html', contexto)

def transportistas_view(request): 
	if request.method == 'POST':
		form = TransportistaForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = TransportistaForm()

	return render(request, 'transportistas/index.html', {'form':form})