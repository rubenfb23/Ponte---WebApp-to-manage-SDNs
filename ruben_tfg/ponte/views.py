from django.shortcuts import render, get_object_or_404
from .models import Red, Ancla
from .forms import RedForm, AnclaForm
from django.http import HttpResponse
from django import forms


def index(request):
    redes = Red.objects.all()
    anclas = Ancla.objects.all()
    return render(request, 'index.html', {
        'redes': redes,
        'anclas': anclas,
    })


def red(request, id_red):
    red = get_object_or_404(Red, pk=id_red)
    dispositivos = red.dispositivos.all()
    return render(request, 'red.html', {
        'red': red,
        'dispositivos': dispositivos,
    })


def ancla(request, id_ancla):
    ancla = get_object_or_404(Ancla, pk=id_ancla)
    return render(request, 'ancla.html', {
        'ancla': ancla,
    })


def crear_red(request, latitud, longitud):
    context = {}

    form = RedForm(request.POST or None)
    if form.is_valid():
        form.save()

    form.fields['latitud'].initial = latitud
    form.fields['longitud'].initial = longitud
    form.fields['estado'].initial = False
    form.fields['estado'].widget = forms.HiddenInput()

    context['form'] = form
    return render(request, 'crear_red.html', {
        'form': form,
    })


def crear_ancla(request, latitud, longitud):
    context = {}

    form = AnclaForm(request.POST or None)
    if form.is_valid():
        form.save()

    form.fields['latitud'].initial = latitud
    form.fields['longitud'].initial = longitud
    form.fields['estado'].initial = False
    form.fields['estado'].widget = forms.HiddenInput()

    context['form'] = form
    return render(request, 'crear_ancla.html', {
        'form': form,
    })


def grupo(request, id_grupo):
    return HttpResponse("You're looking at grupo %s." % id_grupo)


def crear_grupo(request):
    return render(request, 'crear_grupo.html')


def configuracion(request):
    return HttpResponse("You're looking at configuracion")
