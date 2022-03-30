from dataclasses import field
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        field = ['id','title','url','poster','created']