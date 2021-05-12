from django.urls import path
from . import api




urlpatterns = [
    path('audiofiles/', api.AudioFilesAPI.as_view()),
    path('audiofiles/<int:pk>', api.AudioFilesDetailAPI.as_view()),
]
