# ocr_app/urls.py
from django.urls import path
from .views import OCRDocumentUploadView

urlpatterns = [
    path('', OCRDocumentUploadView.as_view(), name='ocr-upload'),
]
