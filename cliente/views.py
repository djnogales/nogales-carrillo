from django.shortcuts import render, redirect
from cliente.models import Cliente
from cliente.forms import ClienteForm
# Create your views here.

def cliente_index (request): 
	cliente = Cliente.objects.all()
	contexto = {'clientes': cliente}
	return render(request, 'home/blank.html', contexto)

def cliente_view(request): 
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ClienteForm()

	return render(request, 'home/index.html', {'form':form})
