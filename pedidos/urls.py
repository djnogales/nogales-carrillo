from django.contrib import admin
from django.conf.urls import url
from pedidos.views import pedidos_index, pedidos_view, pedidos_prov_index, pedidos_prov_view

urlpatterns = [
    url(r'^$', pedidos_index, name='pedido_index'),
    url(r'^nuevo$', pedidos_view, name='pedidos_crear'),
    url(r'^pedidos_proveedores$', pedidos_prov_index, name='pedido_prov_index'),
    url(r'^nuevo_pedido_proveedor$', pedidos_prov_view, name='pedidos_prov_crear'),
]