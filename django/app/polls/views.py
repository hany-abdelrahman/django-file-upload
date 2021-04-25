from django.shortcuts import render
from rest_framework import generics
from .models import UploadImageTest
from .serializers import ImageSerializer
from django.http import HttpResponse
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
class ImageViewSet(generics.ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer


    def post(self, request, *args, **kwargs):
        file = request.data['image']
        image = UploadImageTest.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)