from django import forms
from django.http import request

from .models import Lots

from artists.models import Artists
from customers.models import Customer
from appraisers.models import Appraisers
from technics.models import Technics


class LotsForm(forms.ModelForm):
    artist = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 280px', 'class': 'form-control'}), max_length=200, required=False)
    customer = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 280px', 'class': 'form-control'}),
                             max_length=200, required=True)

    class Meta:
        model = Lots
        fields = (
            'customer',
            'appraiser',
            'code',
            'worknumber',
            'title',
            'artist',
            'desc',
            'technic',
            'type',
            'size',
            'weight',
            'purchase',
            'price',
            'pay',
            'start',
            'limit',
            'note',
        )

        widgets = {
            # 'customer': forms.Select(attrs={'style': 'width: 280px', 'class': 'form-control', }),
            'appraiser': forms.Select(attrs={'style': 'width: 280px', 'class': 'form-control', }),
            'desc': forms.Textarea(attrs={'rows': 2, 'cols': 30, 'style': 'width: 280px', 'class': 'form-control'}),
            'code': forms.NumberInput(attrs={'style': 'width:15ch', 'class': 'form-control', 'placeholder': 'code'}),
            'worknumber': forms.NumberInput(
                attrs={'style': 'width: 15ch', 'class': 'form-control', 'placeholder': 'worknumber'}),
            'title': forms.TextInput(attrs={'style': 'width: 280px', 'class': 'form-control', 'placeholder': 'title'}),
            'technic': forms.Select(attrs={'style': 'width: 280px', 'class': 'form-control', }),
            'type': forms.Select(attrs={'style': 'width: 280px', 'class': 'form-control', }),
            'size': forms.TextInput(attrs={'style': 'width: 280px', 'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'style': 'width: 280px', 'class': 'form-control'}),
            'purchase': forms.NumberInput(attrs={'style': 'width: 15ch', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'style': 'width: 15ch', 'class': 'form-control'}),
            'pay': forms.NumberInput(attrs={'style': 'width: 15ch', 'class': 'form-control'}),
            'start': forms.NumberInput(attrs={'style': 'width: 15ch', 'class': 'form-control'}),
            'limit': forms.NumberInput(attrs={'style': 'width: 15ch', 'class': 'form-control'}),
            'note': forms.Textarea(attrs={'rows': 4, 'cols': 30, 'style': 'width: 280px', 'class': 'form-control'}),
        }

    def clean_artist(self, commit=True):
        artist = self.cleaned_data.get("artist") or None
        if artist is not None:
            artist, created = Artists.objects.get_or_create(name=artist)
            self.cleaned_data['artist'] = artist
        return artist

    def clean_customer(self, commit=True):
        customer = self.cleaned_data.get("customer")
        if Customer.objects.filter(name=customer).exists():
            customer, created = Customer.objects.get_or_create(name=customer)
            self.cleaned_data['customer'] = customer
        else:
            raise forms.ValidationError(("Customer does not exist! Choose another client!"))
        return customer

    def __init__(self, *args, **kwargs):
        super(LotsForm, self).__init__(*args, **kwargs)
