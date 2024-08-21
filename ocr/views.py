from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import pytesseract
from .serializers import ImageUploadSerializer
import logging

logger = logging.getLogger(__name__)

class OCRView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            try:
                image = Image.open(request.FILES['image'])
                text = pytesseract.image_to_string(image)
                return Response({'extracted_text': text}, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error(f"Error processing image: {e}")
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
