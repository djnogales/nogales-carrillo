from django.shortcuts import render
from pedidos.models import PedidoCliente
from pedidos.forms import PedidoClienteForm
from pedidos.models import PedidoProveedor
from pedidos.forms import PedidoProveedorForm

# Create your views here.

def pedidos_index (request): 
	pedido = PedidoCliente.objects.all()
	contexto = {'pedidosCliente': pedido}
	return render(request, 'pedidos/blank.html', contexto)

def pedidos_view (request):
	if request.method == 'POST':
		form = PedidoClienteForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = PedidoClienteForm()

	return render(request, 'pedidos/index.html', {'form':form})

def pedidos_prov_index (request): 
	pedidoProv = PedidoProveedor.objects.all()
	contexto = {'pedidosProveedor': pedidoProv}
	return render(request, 'pedidos/blank2.html', contexto)

def pedidos_prov_view (request):
	if request.method == 'POST':
		form = PedidoProveedorForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = PedidoProveedorForm()

	return render(request, 'pedidos/index2.html', {'form':form})