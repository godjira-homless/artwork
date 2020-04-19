from django import forms
from django.http import request

from .models import Lots

from artists.models import Artists
from appraisers.models import Appraisers
from technics.models import Technics

class LotsForm(forms.ModelForm):
    # artist = forms.CharField(max_length=100, required=False)

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
            'customer': forms.Select(attrs={'style': 'width: 280px', 'class': 'form-control', }),
            'appraiser': forms.Select(attrs={'style': 'width: 280px', 'class': 'form-control', }),
            'artist': forms.Select(attrs={'style': 'width: 280px', 'class': 'form-control', }),
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


    def __init__(self, *args, **kwargs):
        super(LotsForm, self).__init__(*args, **kwargs)