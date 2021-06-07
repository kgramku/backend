from django.conf import settings
from rest_framework import serializers

MAX_POST_LENGTH = settings.MAX_POST_LENGTH
POST_ACTION_OPTIONS = settings.POST_ACTION_OPTIONS

from .models import Post

class UserRegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField(allow_blank = True, required=False)
    
    def validate_action(self, value):
        value = value.lower().strip() #'Like' => 'like'
        if not value in POST_ACTION_OPTIONS:
            raise serializers.ValidationError('this is not valid action for post')
        return value

