from rest_framework import serializer
from .models import Podcast

class PodcastSerializer(serializer.ModelSerializer):
    class Meta:
        model = Podcast
        fields = (  'id', 
                    'name',
                    'duration', 
                    'uploadedTime',
                    'hosts',
                    'participants')