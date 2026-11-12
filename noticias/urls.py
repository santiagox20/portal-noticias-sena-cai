from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_noticias, name='inicio'),
    path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
    path('archivo/', views.tabla_noticias, name='tabla_noticias'),
]