from django.db import models

# Create your models here.

class AudioFile(models.Model):
    id = models.AutoField(primary_key = True)  #(mandatory, integer, unique)
    title = models.CharField(null=True, max_length=100) #(mandatory, string, cannot be larger than 100 characters)
    author = models.CharField(null=True, max_length=100) #(mandatory, string, cannot be larger than 100 characters)
    narrator = models.CharField(null=True, max_length=100) # (mandatory, string, cannot be larger than 100 characters)
    duration = models.IntegerField(null=True)  #(mandatory, integer, positive)
    uploadedTime = models.DateTimeField(auto_now_add = True)