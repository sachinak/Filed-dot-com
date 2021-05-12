from django.db import models

# Create your models here.
class Songs(models.Model):
    id = models.AutoField(primary_key = True)  #(mandatory, integer, unique)
    name = models.CharField(null=True, max_length=100) #(mandatory, string, cannot be larger than 100 characters)
    duration = models.IntegerField(null=True)  #(mandatory, integer, positive)
    uploadedTime = models.DateTimeField(auto_now_add = True)
   