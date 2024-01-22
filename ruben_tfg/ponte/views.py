from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Red


def index(request):
    redes = Red.objects.all()
    return render(request, 'index.html', {
        'redes': redes,
    })


def red(request, id_red):
    red = list(Red.objects.get(id_red=id_red))
    return JsonResponse(red, safe=False)
