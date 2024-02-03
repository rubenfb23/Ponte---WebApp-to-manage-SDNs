from django import forms
from .models import Network, Anchor


class AnchorForm(forms.ModelForm):

    class Meta:
        model = Anchor
        fields = ('name', 'description',
                  'public_ip', 'latitude', 'longitude', 'status')

    def __init__(self, *args, **kwargs):
        super(AnchorForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['public_ip'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['latitude'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitude'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})


class NetworkForm(forms.ModelForm):

    class Meta:
        model = Network
        fields = ('name', 'description', 'type', 'ip', 'subnet_mask', 'status',
                  'gateway', 'latitude', 'longitude', 'devices')

    def __init__(self, *args, **kwargs):
        super(NetworkForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})
        self.fields['ip'].widget.attrs.update({'class': 'form-control'})
        self.fields['subnet_mask'].widget.attrs.update({'class': 'form-control'})
        self.fields['gateway'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['latitude'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitude'].widget.attrs.update({'class': 'form-control'})
        self.fields['devices'].widget.attrs.update(
            {'class': 'form-control'})
