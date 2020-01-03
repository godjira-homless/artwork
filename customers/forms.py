from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name',
                  'address',
                  'city',
                  'zip',
                  'country',
                  'sale_percent',
                  'buy_percent',
                  'phone',
                  'email',
                  'note',
                  )
