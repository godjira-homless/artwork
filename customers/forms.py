from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        label="name", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

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
                  'bank',
                  'taxnumber',

                  )

        widgets = {
          'note': forms.Textarea(attrs={'rows':1, 'cols':20})
        }



