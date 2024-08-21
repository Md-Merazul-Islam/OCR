from django.db import models

class OCRResult(models.Model):
    image = models.ImageField(upload_to='ocr/images')
    extracted_text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OCR Result from {self.uploaded_at}"
