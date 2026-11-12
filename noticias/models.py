

# Create your models here.
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título de la noticia')
    fecha_ocurrencia = models.DateField(verbose_name='Fecha de ocurrencia')
    lugar = models.CharField(max_length=150, verbose_name='Lugar del acontecimiento')
    descripcion = models.TextField(verbose_name='Descripción detallada')
    imagen = models.ImageField(upload_to='noticias/', verbose_name='Imagen de la noticia')
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_ocurrencia', '-fecha_publicacion']

    def __str__(self):
        return f"{self.titulo} ({self.fecha_ocurrencia})"