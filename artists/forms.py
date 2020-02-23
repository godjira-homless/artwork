from django import forms
from .models import Artists


class ArtistForm(forms.ModelForm):
    name = forms.CharField(
        label="Name:", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'autofocus': 'autofocus'}))
    bio = forms.CharField(
        label="Bio:", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Artists
        fields = ('name',
                  'bio',
                  )
