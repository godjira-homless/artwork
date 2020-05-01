from django import forms
from django.http import request

from .models import Lots

from artists.models import Artists
from customers.models import Customer
from appraisers.models import Appraisers
from technics.models import Technics


class LotsForm(forms.ModelForm):
    artist = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                             max_length=200, required=False)
    customer = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                               max_length=200, required=True)
    appraiser = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                                max_length=200, required=True)
    technic = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                              max_length=200, required=False)

    # photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))

    class Meta:
        model = Lots
        fields = (
            'customer',
            'appraiser',
            'photo',
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
            'desc': forms.Textarea(attrs={'rows': 2, 'cols': 30, 'style': 'width: 220px', 'class': 'form-control'}),
            'code': forms.NumberInput(attrs={'style': 'width:15ch', 'class': 'form-control', 'placeholder': 'code'}),
            'worknumber': forms.NumberInput(
                attrs={'style': 'width: 15ch', 'class': 'form-control', 'placeholder': 'worknumber'}),
            'title': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control', 'placeholder': 'title'}),
            'type': forms.Select(attrs={'style': 'width: 220px', 'class': 'form-control', }),
            'size': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
            'purchase': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_purchase'}),
            'price': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_price'}),
            'pay': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_pay'}),
            'start': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_start'}),
            'limit': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_limit'}),
            'note': forms.Textarea(attrs={'rows': 3, 'cols': 30, 'style': 'width: 220px', 'class': 'form-control'}),
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

    def clean_appraiser(self, commit=True):
        appraiser = self.cleaned_data.get("appraiser")
        if Appraisers.objects.filter(name=appraiser).exists():
            appraiser, created = Appraisers.objects.get_or_create(name=appraiser)
            self.cleaned_data['appraiser'] = appraiser
        else:
            raise forms.ValidationError("Appraiser does not exist! Choose another one!")
        return appraiser

    def clean_technic(self, commit=True):
        technic = self.cleaned_data.get("technic") or None
        if technic is not None:
            technic, created = Technics.objects.get_or_create(name=technic)
            self.cleaned_data['technic'] = technic
        return technic

    def clean_purchase(self, commit=True):
        purchase = self.cleaned_data.get("purchase") or None
        pur = str(purchase)
        purchase = pur.replace(",", '')
        return purchase

    def clean_price(self, commit=True):
        price = self.cleaned_data.get("price") or None
        pur = str(price)
        price = pur.replace(",", '')
        return price

    def clean_pay(self, commit=True):
        pay = self.cleaned_data.get("pay") or None
        pur = str(pay)
        pay = pur.replace(",", '')
        return pay

    def clean_start(self, commit=True):
        start = self.cleaned_data.get("start") or None
        pur = str(start)
        start = pur.replace(",", '')
        return start

    def clean_limit(self, commit=True):
        limit = self.cleaned_data.get("limit") or None
        pur = str(limit)
        limit = pur.replace(",", '')
        return limit

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
