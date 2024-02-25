from rest_framework import serializers
from .models import TranslationRequest

class TranslationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationRequest
        fields = ['requester_name', 'email', 'phone', 'description']