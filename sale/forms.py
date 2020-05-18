from django.forms import Field
from django import forms
from django.http import request
from django.utils.translation import gettext as _

from .models import Sales
from customers.models import Customer
from lots.models import Lots


class SaleSelector(forms.Form):

    selcode = forms.CharField(label=_('Code'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=True,)

    def __init__(self, *args, **kwargs):
        super(SaleSelector, self).__init__(*args, **kwargs)

    def clean_selcode(self, commit=True):
        selcode = self.cleaned_data.get("selcode")
        if Sales.objects.filter(code=selcode).exists():
            raise forms.ValidationError("Lots exist! You can not sold an item more than once!")
        if Lots.objects.filter(code=selcode).exists():
            selcode = Lots.objects.get(code=selcode)
            self.cleaned_data['selcode'] = selcode
        else:
            raise forms.ValidationError("Lot does not exist! Choose another Lot!")
        return selcode


class SalesForm(forms.ModelForm):
    buyer = forms.CharField(label=_('Buyer'),
                               widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                               max_length=220, required=True)
    code = forms.CharField(label=_('Code'),
                           widget=forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
                           max_length=220, required=True,)

    sold = forms.CharField(label=_('Sold'),
                           widget=forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_sold'}),
                           required=True)

    pay = forms.CharField(label=_('Pay'),
                           widget=forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_pay'}),
                           required=True)

    purchase = forms.CharField(label=_('Purchase'),
                           widget=forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_purchase'}),
                           required=False)
    class Meta:
        model = Sales
        fields = (
            'buyer',
            'code',
            'invoice',
            'customer_invoice',
            'vjegy',
            'sale_date',
            'note',
        )

        widgets = {
            # 'code': forms.NumberInput(attrs={'style': 'width:15ch', 'class': 'form-control', 'placeholder': 'code'}),
            # 'purchase': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_purchase'}),
            # 'pay': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_pay'}),
            # 'sold': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-num_sold'}),
            'invoice': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control', }),
            'customer_invoice': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control', }),
            'sale_date': forms.TextInput(attrs={'style': 'width: 15ch', 'class': 'form-control input-sale_date'}),
            'note': forms.Textarea(attrs={'rows': 3, 'cols': 30, 'style': 'width: 220px', 'class': 'form-control'}),
            'vjegy': forms.TextInput(attrs={'style': 'width: 220px', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['readonly'] = True

    def clean_buyer(self, commit=True):
        buyer = self.cleaned_data.get("buyer")
        if Customer.objects.filter(name=buyer).exists():
            buyer = Customer.objects.get(name=buyer)
            self.cleaned_data['buyer'] = buyer
        else:
            raise forms.ValidationError("Customer does not exist! Choose another client!")
        return buyer

    def clean_purchase(self, commit=True):
        purchase = self.cleaned_data.get("purchase")
        if purchase:
            pur = str(purchase)
            purchase = pur.replace(",", '')
            purchase = int(purchase)
        else:
            purchase = None
        return purchase

    def clean_pay(self, commit=True):
        pay = self.cleaned_data.get("pay")
        if pay:
            pur = str(pay)
            pay = pur.replace(",", '')
            pay = int(pay)
        else:
            pay = None
        return pay

    def clean_sold(self, commit=True):
        sold = self.cleaned_data.get("sold")
        if sold:
            pur = str(sold)
            sold = pur.replace(",", '')
            sold = int(sold)
        else:
            sold = None
        return sold

    def clean_code(self, commit=True):
        code = self.cleaned_data.get("code")
        if Lots.objects.filter(code=code).exists():
            code = Lots.objects.get(code=code)
            self.cleaned_data['code'] = code
        else:
            raise forms.ValidationError("Lots does not exist! Choose another client!")
        return code


