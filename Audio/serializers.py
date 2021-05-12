from rest_framework import serializers
from .models import AudioFile, Podcast, Songs

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = (  'id', 
                    'name',
                    'duration', 
                    'uploadedTime')




class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = (  'id', 
                    'name',
                    'duration', 
                    'uploadedTime',
                    'hosts',
                    'participants')

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = (  'id', 
                  'title',
                    'author', 
                    'narrator', 
                    'duration', 
                    'uploadedTime')