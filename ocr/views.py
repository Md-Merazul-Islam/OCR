# ocr_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import pytesseract
from PIL import Image
from .models import OCRDocument
from .serializers import OCRDocumentSerializer

class OCRDocumentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = OCRDocumentSerializer(data=request.data)
        if file_serializer.is_valid():
            ocr_document = file_serializer.save()
            image = Image.open(ocr_document.image)
            text = pytesseract.image_to_string(image)
            ocr_document.text = text
            ocr_document.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
