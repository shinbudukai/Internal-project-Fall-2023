from dataclasses import field
from rest_framework import serializers
from .models import languageDetect

class GetAllLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = languageDetect
        fields = ("language", "confidence", "reliable")