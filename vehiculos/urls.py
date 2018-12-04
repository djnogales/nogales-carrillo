from django.contrib import admin
from django.conf.urls import url
from vehiculos.views import vehiculos_index, vehiculos_view

urlpatterns = [
    url(r'^$', vehiculos_index, name='vehiculos_index'),
    url(r'^nuevo$', vehiculos_view, name='vehiculos_crear'),
]