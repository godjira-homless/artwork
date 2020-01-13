from django import forms
from .models import Technics


class TechnicForm(forms.ModelForm):
    name = forms.CharField(
        label="Név:", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'autofocus': 'autofocus'}))

    class Meta:
        model = Technics
        fields = ('name',
                  )
