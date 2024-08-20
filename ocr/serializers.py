# ocr_app/serializers.py
from rest_framework import serializers
from .models import OCRDocument

class OCRDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRDocument
        fields = ('id', 'image', 'text', 'uploaded_at')
