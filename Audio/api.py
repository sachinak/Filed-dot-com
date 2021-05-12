from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AudioFile, Songs, Podcast
from .serializers import AudioFileSerializer, SongsSerializer, PodcastSerializer

class AudioAPI(APIView):

    def get(self, request, type = None, id = None):
        if not type:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if type == 'song':
            if not id:
                queryset = Songs.objects.all()
                serializer = SongsSerializer(queryset, many = True)
            else:
                queryset = Songs.objects.get(id = id)
                serializer = SongsSerializer(queryset)

        elif type == 'audiofile':
            if not id:
                queryset = AudioFile.objects.all()
                serializer = AudioFileSerializer(queryset, many = True)
            else:
                queryset = Audio.objects.get(id = id)
                serializer = AudioFileSerializer(queryset)

        elif type == 'podcast':
            if not id:
                queryset = Podcast.objects.all()
                serializer = PodcastSerializer(queryset, many = True)
            else:
                queryset = Podcast.objects.get(id = id)
                serializer = PodcastSerializer(queryset)
        
        return Response(serializer.data, status = status.HTTP_200_OK)

        


    def post(self, request, type = None, id = None):
        if not type:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if type == 'song':
            serializer = SongsSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                
        
        elif type == 'audiofile':           
            serializer = AudioFileSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                
        elif type == 'podcast':
            serializer = PodcastSerializer(data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, type = None, id = None):
        if not type or not id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if type == 'song':
            queryset = Songs.objects.get(id = id)
            serializer = SongsSerializer(queryset, data = request.data, partial = True)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                
        
        elif type == 'audiofile':    
            queryset = AudioFile.objects.get(id = id)       
            serializer = AudioFileSerializer(queryset, data = request.data, partial = True)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                
        elif type == 'podcast':
            queryset = Podcast.objects.get(id = id)
            serializer = PodcastSerializer(queryset, data = request.data, partial = True)
            if serializer.is_valid(raise_exception = True):
                serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, type = None, id = None):
        if not type or not id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if type == 'song':
            queryset = Songs.objects.get(id = id)
            queryset.delete()                
        
        elif type == 'audiofile':    
            queryset = AudioFile.objects.get(id = id)       
            queryset.delete()
                
        elif type == 'podcast':
            queryset = Podcast.objects.get(id = id)
            queryset.delete()

        return Response(status = status.HTTP_200_OK)