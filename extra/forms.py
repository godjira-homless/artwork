from django import forms
from django.http import request
from django.utils.translation import gettext as _
from .models import Extras

from artists.models import Artists
from appraisers.models import Appraisers
from customers.models import Customer
from technics.models import Technics


class ExtrasForm(forms.ModelForm):

    customer = forms.CharField(label=_('Customer'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=False)
    artist = forms.CharField(label=_('Atrist'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=False)
    appraiser = forms.CharField(label=_('Appraiser'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=False)
    technic = forms.CharField(label=_('Technic'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=False)
    title = forms.CharField(label=_('Title'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=False)
    worknumber = forms.CharField(label=_('Worknumber'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=False)

    class Meta:
        model = Extras
        fields = (
            'artist',
            'appraiser',
            'customer',
            'title',
            'technic',
            'worknumber',
                  )

    def clean_artist(self, commit=True):
        artist = self.cleaned_data.get("artist") or None
        if artist is not None:
            artist, created = Artists.objects.get_or_create(name=artist)
            self.cleaned_data['artist'] = artist
        return artist

    def clean_customer(self, commit=True):
        customer = self.cleaned_data.get("customer") or None
        if customer is None:
            customer = None
        else:
            if Customer.objects.filter(name=customer).exists():
                customer, created = Customer.objects.get_or_create(name=customer)
                self.cleaned_data['customer'] = customer
            else:
                raise forms.ValidationError(("Customer does not exist! Choose another client!"))
        return customer

    def clean_appraiser(self, commit=True):
        appraiser = self.cleaned_data.get("appraiser") or None
        if appraiser is None:
          appraiser = None
        else:
            if Appraisers.objects.filter(name=appraiser).exists():
                appraiser, created = Appraisers.objects.get_or_create(name=appraiser)
                self.cleaned_data['appraiser'] = appraiser
            else:
                raise forms.ValidationError("Appraiser does not exist! Choose another one!")
        return appraiser

    def clean_technic(self, **kwargs):
        technic = self.cleaned_data.get("technic") or None
        if technic is not None:
            technic, created = Technics.objects.get_or_create(name=technic)
            self.cleaned_data['technic'] = technic
        return technic

    def clean_worknumber(self):
        worknumber = self.cleaned_data.get("worknumber") or None
        return worknumber

    def __init__(self, *args, **kwargs):
        super(ExtrasForm, self).__init__(*args, **kwargs)