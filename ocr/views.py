from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import pytesseract
from .serializers import ImageUploadSerializer
from .models import OCRResult

class OCRView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            try:
                image_file = request.FILES['image']
                image = Image.open(image_file)
                text = pytesseract.image_to_string(image)

                ocr_result = OCRResult.objects.create(image=image_file, extracted_text=text)
                return Response({'extracted_text': ocr_result.extracted_text}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OCRResultListView(APIView):
    def get(self, request, *args, **kwargs):
        results = OCRResult.objects.all()
        data = [{'id': result.id, 'extracted_text': result.extracted_text, 'uploaded_at': result.uploaded_at} for result in results]
        return Response(data, status=status.HTTP_200_OK)
