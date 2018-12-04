from django.contrib import admin
from django.conf.urls import url
from cliente.views import cliente_index, cliente_view

urlpatterns = [
    url(r'^$', cliente_index, name='index'),
    url(r'^nuevo$', cliente_view, name='cliente_crear'),
]