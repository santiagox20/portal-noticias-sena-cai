

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Noticia

# Personalización de encabezados del Panel Administrativo
admin.site.site_header = "Administración Portal SENA - CAI Regional Valle"
admin.site.site_title = "Portal SENA Admin"
admin.site.index_title = "Gestión de Noticias y Contenidos Institucionales"


class NoticiaAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado
    list_display = ('miniatura_imagen', 'titulo', 'lugar', 'fecha_ocurrencia', 'badge_reciente')
    # Enlaces clicables para entrar a editar
    list_display_links = ('miniatura_imagen', 'titulo')
    # Filtros laterales
    list_filter = ('fecha_ocurrencia', 'lugar')
    # Barra de búsqueda por múltiples campos
    search_fields = ('titulo', 'lugar', 'descripcion')
    # Orden por fecha más reciente
    ordering = ('-fecha_ocurrencia',)
    # Navegación jerárquica por fechas en la parte superior
    date_hierarchy = 'fecha_ocurrencia'
    # Paginación en el admin
    list_per_page = 10
    # Campos de solo lectura
    readonly_fields = ('fecha_publicacion', 'vista_previa_formulario')

    # Organización visual del formulario de creación/edición
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'lugar', 'fecha_ocurrencia')
        }),
        ('Contenido y Multimedia', {
            'fields': ('descripcion', 'imagen', 'vista_previa_formulario')
        }),
        ('Auditoría del Sistema', {
            'fields': ('fecha_publicacion',),
            'classes': ('collapse',)
        }),
    )

    @admin.display(description='Vista Previa')
    def miniatura_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width: 70px; height: 48px; object-fit: cover; border-radius: 6px; border: 1px solid #ddd;" />',
                obj.imagen.url
            )
        return "Sin imagen"

    @admin.display(description='Imagen Actual')
    def vista_previa_formulario(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 200px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.15);" />',
                obj.imagen.url
            )
        return "Aún no se ha cargado una imagen."

    @admin.display(description='Estado', ordering='fecha_ocurrencia')
    def badge_reciente(self, obj):
        from datetime import date, timedelta
        if obj.fecha_ocurrencia >= date.today() - timedelta(days=7):
            return format_html(
                '<span style="background-color: #39A900; color: white; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: bold;">Reciente</span>'
            )
        return format_html(
            '<span style="background-color: #6c757d; color: white; padding: 3px 8px; border-radius: 12px; font-size: 11px;">Archivo</span>'
        )


admin.site.register(Noticia, NoticiaAdmin)