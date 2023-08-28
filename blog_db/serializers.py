from rest_framework import serializers

from .models import *

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'article',
            'image1',
            'image2',
            'image3',
            'date'
        ]