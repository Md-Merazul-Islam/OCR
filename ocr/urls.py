from django.urls import path
from .views import OCRView, OCRResultListView

urlpatterns = [
    path('ocr/', OCRView.as_view(), name='ocr'),
    path('results/', OCRResultListView.as_view(), name='ocr-results'),
]
