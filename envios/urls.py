from django.contrib import admin
from django.conf.urls import url
from envios.views import envios_cliente_index, envios_cliente_view

urlpatterns = [
    url(r'^$', envios_cliente_index, name='envios_cliente_index'),
   	url(r'^nuevo$', envios_cliente_view, name='asignar_envio'),
]