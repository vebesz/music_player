from django import forms
from django.forms import ModelForm

from .models import Music

# music upload form


class UploadForm(ModelForm):
    forms.FloatField(required=False)

    class Meta:
        model = Music
        fields = [
            'title', 'artist', 'image', 'audio'
        ]
