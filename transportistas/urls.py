from django.contrib import admin
from django.conf.urls import url
from transportistas.views import transportistas_index, transportistas_view

urlpatterns = [
    url(r'^$', transportistas_index, name='transportista_index'),
    url(r'^nuevo$', transportistas_view, name='transportista_crear'),
]