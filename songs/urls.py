from django.urls import path
from . import api




urlpatterns = [
    path('songs/', api.SongsAPI.as_view()),
    path('songs/<int:pk>', api.SongsDetailAPI.as_view()),
]
