from django.db import models
from django.conf import settings

User= settings.AUTH_USER_MODEL
# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, null=True,blank= True)
    kuDepartment= models.CharField(max_length=200,null=True, blank=True)



