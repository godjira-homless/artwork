from django import forms
from django.http import request

from .models import Extras

from artists.models import Artists


class ExtrasForm(forms.ModelForm):
    artist = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Extras
        fields = (
            'artist',
                  )

    def clean_artist(self, commit=True):
        artist = self.cleaned_data.get("artist")
        artist, created = Artists.objects.get_or_create(name=artist)
        self.cleaned_data['artist'] = artist
        return artist

    def __init__(self, *args, **kwargs):
        super(ExtrasForm, self).__init__(*args, **kwargs)
