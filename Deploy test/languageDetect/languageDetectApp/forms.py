from dataclasses import field
from .models import languageDetect
from django.forms import ModelForm

class langyageDetectForm(ModelForm):
    class Meta:
        model = languageDetect
        field = '__all__'