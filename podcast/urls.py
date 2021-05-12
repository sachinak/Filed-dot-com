from django.urls import path
from . import api




urlpatterns = [
    path('podcast/', api.PodcastAPI.as_view()),
    path('podcast/<int:pk>', api.PodcastDetailAPI.as_view()),
]

