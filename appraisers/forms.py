from django import forms
from .models import Appraisers


class AppraiserForm(forms.ModelForm):
    name = forms.CharField(
        label="Name:", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'autofocus': 'autofocus'}))

    class Meta:
        model = Appraisers
        fields = ('name',
                  )
