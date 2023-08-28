from rest_framework import serializers

from .models import *

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'article_title',
            'article',
            'image1',
            'image2',
            'image3',
            'date'
        ]

    def create(self, validated_data):

        return Blog.objects.create(**validated_data)