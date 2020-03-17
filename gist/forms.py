from django.forms import ModelForm
from .models import *

class GistForm(ModelForm):
    class Meta:
        model = Gist
        fields = [
            'gists',
            'gistImage',
        ]



