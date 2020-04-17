from django import forms
from django.http import request

from .models import Lots

from artists.models import Artists
from appraisers.models import Appraisers
from technics.models import Technics


class LotsForm(forms.ModelForm):
    artist = forms.CharField(max_length=100, required=False)

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
                  )

    def __init__(self, *args, **kwargs):
        super(LotsForm, self).__init__(*args, **kwargs)
