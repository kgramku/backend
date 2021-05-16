from django.conf import settings
from rest_framework import serializers

MAX_POST_LENGTH = settings.MAX_POST_LENGTH
POST_ACTION_OPTIONS = settings.POST_ACTION_OPTIONS

from .models import Post

class PostActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank = True, required=False)
    
    def validate_action(self, value):
        value = value.lower().strip() #'Like' => 'like'
        if not value in POST_ACTION_OPTIONS:
            raise serializers.ValidationError('this is not valid action for post')
        return value

class PostCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['id','content', 'image','likes']
       # field = ['content']
    def get_likes(self,obj):
        return obj.likes.count()
        
    def validate(self,value):       
        if len(value['content']) > MAX_POST_LENGTH:           
            raise serializers.ValidationError({'content': 'post too long'})
        return value


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = PostCreateSerializer(read_only=True)
    # content = serializers.SerializerMethodField(read_only=True)
   #not_required is_repost= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['id','content', 'image','likes','is_repost', 'parent']
       # field = ['content']
    def get_likes(self,obj):
        return obj.likes.count()

    # def get_content(self,obj):
    #     content = obj.content
    #     if obj.is_repost:
    #         content = obj.parent.content
    #     return content
        
    

    