from django.contrib import admin
from django.conf.urls import url
from proveedores.views import proveedores_index, proveedores_view

urlpatterns = [
    url(r'^$', proveedores_index, name='proveedores_index'),
    url(r'^nuevo$', proveedores_view, name='proveedor_crear'),
]