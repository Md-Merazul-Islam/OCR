from rest_framework import viewsets, status
from rest_framework.response import Response
from PIL import Image
import pytesseract
import cv2
from .serializers import ImageUploadSerializer, OCRResultSerializer
from .models import OCRResult

class OCRViewSet(viewsets.ModelViewSet):
    queryset = OCRResult.objects.all()
    serializer_class = OCRResultSerializer

    def create(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            try:
                image_file = request.FILES['image']
                image = Image.open(image_file)
                text = pytesseract.image_to_string(image)

                # Save the result to the database
                ocr_result = OCRResult.objects.create(image=image_file, extracted_text=text)

                # Return the OCR result
                return Response({'extracted_text': ocr_result.extracted_text}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        results = OCRResult.objects.all()
        serializer = OCRResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
