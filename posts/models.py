from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL
# Create your models here.

class PostLike(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey('Post', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add= True)

class Post(models.Model):
    parent = models.ForeignKey("self",null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #many users can have many posts, CASCADE= if owner is gone all their post is gone
    likes= models.ManyToManyField(User, related_name='post_user', blank=True, through= PostLike)
    content = models.TextField(blank = True, null= True)
    image = models.FileField(upload_to='images/', blank =True, null = True)
    timestamp = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-id']
    
    @property
    def is_repost(self):
        return self.parent != None #if parent is not equal to none then it is repost

    def serialize(self):
        '''feel free to delete'''
        return{
            "id": self.id,
            "content": self.content,
            "likes" : random.randint(0,200)

        }
