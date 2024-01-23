from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Red, Grupo, Dispositivo, Servicio


def index(request):
    redes = Red.objects.all()
    return render(request, 'index.html', {
        'redes': redes,
    })


def red(request, id_red):
    red = get_object_or_404(Red, pk=id_red)
    return render(request, 'red.html', {
        'red': red,
    })


def crear_red(request, latitud, longitud):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'crear_red.html', {
        'latitud': latitud,
        'longitud': longitud,
        'dispositivos': dispositivos,
    })


def grupo(request, id_grupo):
    return HttpResponse("You're looking at grupo %s." % id_grupo)


def crear_grupo(request):
    return render(request, 'crear_grupo.html')


def configuracion(request):
    return HttpResponse("You're looking at configuracion")
