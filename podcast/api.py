from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PodcastAPI(APIView):

    def get(self, request):
        pass
    
    def post(self, request):
        pass


class PodcastDetailAPI(APIView):

    def get(self, request, pk):
        pass
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass