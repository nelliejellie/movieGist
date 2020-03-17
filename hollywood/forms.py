from django.forms import ModelForm
from .models import *

class movieform(ModelForm):
    class Meta:
        model = Movies
        fields = [
            'name',
            'image',
            'description',
            'year_of_release',
            'date',
        ]

class tvShowform(ModelForm):
    class Meta:
        model = Tvshows
        fields = [
            'name',
            'image',
            'description',
            'season',
            'episode',
            'year_of_release',
            'date',
        ]


class gistform(ModelForm):
    class Meta:
        model = gist
        fields = [
            'gists',
            'date',
        ]