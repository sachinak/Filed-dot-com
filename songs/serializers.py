from rest_framework import serializer
from .models import AudioFile

class SongsSerializer(serializer.ModelSerializer):
    class Meta:
        model = Songs
        fields = (  'id', 
                    'name',
                    'duration', 
                    'uploadedTime')