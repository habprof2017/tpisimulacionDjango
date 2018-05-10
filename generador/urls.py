from django.conf.urls import url
from generador.views import *

urlpatterns = [
    url(r'^$', inicio, name="inicio"),
    url(r'^lote1$', generadorLote1, name="generarLote1"),
    url(r'^lote2$', generadorLote2, name="generarLote2"),
    url(r'^historial/lote1$', HistorialLote1.as_view(), name='historial1'),
    url(r'^historial/lote2$', HistorialLote2.as_view(), name='historial2'),
]
