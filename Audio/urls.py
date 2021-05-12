from django.urls import path
from . import api




urlpatterns = [
    path('audio/<str:type>/<int:id>', api.AudioAPI.as_view()),
    path('audio/<str:type>', api.AudioAPI.as_view()),
]
