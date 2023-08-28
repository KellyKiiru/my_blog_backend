from django.http import HttpResponse
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.

def home(request):
    return HttpResponse("Blog is working")

class GetBlogs(APIView):

    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)
