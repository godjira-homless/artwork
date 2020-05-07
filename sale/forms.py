from django.forms import Field
from django import forms
from django.http import request
from django.utils.translation import gettext as _

from .models import Sales
from customers.models import Customer
from lots.models import Lots


class SalesForm(forms.ModelForm):
    customer = forms.CharField(label=_('Customer'),
                               widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                               max_length=220, required=True)
    code = forms.CharField(label=_('Code'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=True)

    class Meta:
        model = Sales
        fields = (
            'customer',
            'code',
            'purchase',
            'sold',
            'pay',
            'invoice',
            'customer_invoice',
            'vjegy',
            'sale_date',
            'note',
        )

        widgets = {
            'code': forms.NumberInput(attrs={'style': 'width:15ch', 'class': 'form-control', 'placeholder': 'code'}),
            'purchase': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_purchase'}),
            'pay': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_pay'}),
            'sold': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_sold'}),
            'invoice': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control', }),
            'customer_invoice': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control', }),
            'sale_date': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-sale_date'}),
            'note': forms.Textarea(attrs={'rows': 3, 'cols': 30, 'style': 'width: 220px', 'class': 'form-control'}),
            'vjegy': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)

    def clean_customer(self, commit=True):
        customer = self.cleaned_data.get("customer")
        if Customer.objects.filter(name=customer).exists():
            customer = Customer.objects.get(name=customer)
            self.cleaned_data['customer'] = customer
        else:
            raise forms.ValidationError("Customer does not exist! Choose another client!")
        return customer

    def clean_code(self, commit=True):
        code = self.cleaned_data.get("code")
        if Lots.objects.filter(code=code).exists():
            code = Lots.objects.get(code=code)
            self.cleaned_data['code'] = code
        else:
            raise forms.ValidationError("Lot does not exist! Choose another Lot!")
        return code

    def clean_purchase(self, commit=True):
        purchase = self.cleaned_data.get("purchase") or None
        pur = str(purchase)
        purchase = pur.replace(",", '')
        return purchase

    def clean_pay(self, commit=True):
        pay = self.cleaned_data.get("pay") or None
        pur = str(pay)
        pay = pur.replace(",", '')
        return pay

    def clean_sold(self, commit=True):
        sold = self.cleaned_data.get("sold") or None
        pur = str(sold)
        sold = pur.replace(",", '')
        return sold

