from django import forms
from django.http import request

from .models import Extras

from artists.models import Artists
from appraisers.models import Appraisers
from technics.models import Technics


class ExtrasForm(forms.ModelForm):
    artist = forms.CharField(max_length=100, required=False)
    appraiser = forms.CharField(max_length=100, required=False)
    technic = forms.CharField(max_length=100, required=False)
    ai = forms.CharField(max_length=100, required=False, widget=forms.HiddenInput())
    title = forms.CharField(max_length=255, required=False)
    worknumber = forms.IntegerField(required=False)

    class Meta:
        model = Extras
        fields = (
            'artist',
            'ai',
            'appraiser',
            'technic',
            'title',
            'worknumber',
                  )

    def clean_ai(self):
        ai = self.cleaned_data.get("ai")
        return ai

    def clean_artist(self, commit=True):
        # artist = self.cleaned_data.get("artist")
        aid = self.data['ai']
        artist, created = Artists.objects.get_or_create(pk=aid)
        self.cleaned_data['artist'] = artist
        return artist

    def clean_appraiser(self, commit=True):
        appraiser = self.cleaned_data.get("appraiser")
        appraiser, created = Appraisers.objects.get_or_create(name=appraiser)
        self.cleaned_data['appraiser'] = appraiser
        return appraiser

    def clean_technic(self, commit=True):
        technic = self.cleaned_data.get("technic")
        technic, created = Technics.objects.get_or_create(name=technic)
        self.cleaned_data['technic'] = technic
        return technic

    def clean_title(self, commit=True):
        title = self.cleaned_data.get("title")
        return title

    def clean_worknumber(self, commit=True):
        worknumber = self.cleaned_data.get("worknumber")
        return worknumber

    def __init__(self, *args, **kwargs):
        super(ExtrasForm, self).__init__(*args, **kwargs)
