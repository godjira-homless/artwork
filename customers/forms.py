from django import forms
from .models import Customer

my_default_errors = {
    'required': 'A mező kitöltése kötelező',
    'invalid': 'Nem érvényes érték'
}

class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        label="Név:", required=True, error_messages=my_default_errors,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'autofocus': 'autofocus'}))
    address = forms.CharField(
        label="address", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    city = forms.CharField(
        label="city", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    zip = forms.CharField(
        label="zip", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    country = forms.CharField(
        label="country", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    bank = forms.CharField(
        label="bank", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    phone = forms.CharField(
        label="phone", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    email = forms.EmailField(
        label="email", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    taxnumber = forms.CharField(
        label="taxnumber", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    sale_percent = forms.CharField(
        label="sale_percent", initial=21, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    buy_percent = forms.CharField(
        label="buy_percent", initial=15, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-sm'}))
    note = forms.Textarea(attrs={'class': 'form-control  form-control-sm'})

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
            'note': forms.Textarea(attrs={'rows': 3, 'cols': 25})
        }
