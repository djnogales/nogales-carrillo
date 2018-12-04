from django.shortcuts import render
from envios.models import EnvioCliente
from envios.forms import EnvioClienteForm
from facturas.models import Factura
# Create your views here.
def envios_cliente_index (request): 
	envioCliente = EnvioCliente.objects.all()
	contexto = {'enviosCliente': envioCliente}
	return render(request, 'envios/blank.html', contexto)

def envios_cliente_view (request):
	if request.method == 'POST':
		form = EnvioClienteForm(request.POST)
		if form.is_valid():
			envioCl = form.save()
			factura = Factura.objects.create (envio = envioCl, cliente = envioCl.pedido.cliente,importe = 300,  estado = 'Fraccionada', fecha = '2018-12-04', pagada = False)
			factura.save()
	else:
		form = EnvioClienteForm()

	return render(request, 'envios/index.html', {'form':form})