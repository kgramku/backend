from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #many users can have many posts, CASCADE= if owner is gone all their post is gone
    content = models.TextField(blank = True, null= True)
    image = models.FileField(upload_to='images/', blank =True, null = True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return{
            "id": self.id,
            "content": self.content,
            "likes" : random.randint(0,200)

        }
