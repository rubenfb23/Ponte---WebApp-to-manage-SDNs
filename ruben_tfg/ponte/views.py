from django.shortcuts import render, get_object_or_404
from .models import Network, Anchor
from .forms import NetworkForm, AnchorForm
from django.http import HttpResponse
from django import forms


def index(request):
    networks = Network.objects.all()
    anchors = Anchor.objects.all()
    return render(request, 'index.html', {
        'networks': networks,
        'anchors': anchors,
    })


def network(request, network_id):
    network = get_object_or_404(Network, pk=network_id)
    devices = network.devices.all()
    return render(request, 'network.html', {
        'network': network,
        'devices': devices,
    })


def anchor(request, anchor_id):
    anchor = get_object_or_404(Anchor, pk=anchor_id)
    return render(request, 'anchor.html', {
        'anchor': anchor,
    })


def create_network(request, latitude, longitude):
    context = {}

    form = NetworkForm(request.POST or None)
    if form.is_valid():
        form.save()

    form.fields['latitude'].initial = latitude
    form.fields['longitude'].initial = longitude
    form.fields['status'].initial = False
    form.fields['status'].widget = forms.HiddenInput()

    context['form'] = form
    return render(request, 'create_network.html', {
        'form': form,
    })


def create_anchor(request, latitude, longitude):
    context = {}

    form = AnchorForm(request.POST or None)
    if form.is_valid():
        form.save()

    form.fields['latitude'].initial = latitude
    form.fields['longitude'].initial = longitude
    form.fields['status'].initial = False
    form.fields['status'].widget = forms.HiddenInput()

    context['form'] = form
    return render(request, 'create_anchor.html', {
        'form': form,
    })


def group(request, group_id):
    return HttpResponse("You're looking at group %s." % group_id)


def create_group(request):
    return render(request, 'create_group.html')


def configuration(request):
    return HttpResponse("You're looking at configuration")
