from rest_framework import serializers
from .models import OCRResult

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()

class OCRResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRResult
        fields = ['id', 'image', 'extracted_text', 'uploaded_at']
