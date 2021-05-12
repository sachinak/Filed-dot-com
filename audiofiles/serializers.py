from rest_framework import serializer
from .models import AudioFile

class AudioFileSerializer(serializer.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = (  'id', 
                    'title',
                    'author', 
                    'narrator', 
                    'duration', 
                    'uploadedTime')