from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

class Podcast(models.Model):
    id = models.AutoField(primary_key = True)  #(mandatory, integer, unique)
    name = models.CharField(null=True, max_length=100) #(mandatory, string, cannot be larger than 100 characters)
    duration = models.IntegerField(null=True)  #(mandatory, integer, positive)
    uploadedTime = models.DateTimeField(auto_now_add = True)
    host = models.CharField(null=True, max_length=100) 
    participants = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(10 * 101)  
    )
   