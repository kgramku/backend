from django.conf import settings
from rest_framework import serializers

MAX_POST_LENGTH = settings.MAX_POST_LENGTH

from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
       # field = ['content']

    def validate_content(self,value):
        print('helo')
        if len(value) > MAX_POST_LENGTH:
            print('if bhitra')
            raise serializers.ValidationError("post too long")
        print(value)
        return value

    