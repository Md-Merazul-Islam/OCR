# ocr_app/models.py
from django.db import models

class OCRDocument(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
