

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Noticia


def lista_noticias(request):
    busqueda = request.GET.get('q', '').strip()
    lugar_filtro = request.GET.get('lugar', '').strip()

    noticias = Noticia.objects.all()

    if busqueda:
        noticias = noticias.filter(
            Q(titulo__icontains=busqueda) |
            Q(lugar__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )

    if lugar_filtro:
        noticias = noticias.filter(lugar__iexact=lugar_filtro)

    lugares_disponibles = (
        Noticia.objects.values_list('lugar', flat=True)
        .distinct()
        .order_by('lugar')
    )

    contexto = {
        'noticias': noticias,
        'busqueda': busqueda,
        'lugar_filtro': lugar_filtro,
        'lugares_disponibles': lugares_disponibles,
        'total_noticias': noticias.count(),
    }
    return render(request, 'inicio.html', contexto)


def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    recientes = Noticia.objects.exclude(id=noticia.id)[:3]

    contexto = {
        'noticia': noticia,
        'recientes': recientes,
    }
    return render(request, 'detalle_noticia.html', contexto)


def tabla_noticias(request):
    noticias = Noticia.objects.all()
    contexto = {
        'noticias': noticias,
    }
    return render(request, 'tabla_noticias.html', contexto)