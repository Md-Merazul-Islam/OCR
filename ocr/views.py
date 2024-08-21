from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
import pytesseract
from .serializers import ImageUploadSerializer

class OCRView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = Image.open(request.FILES['image'])
            text = pytesseract.image_to_string(image)
            return Response({'extracted_text': text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
