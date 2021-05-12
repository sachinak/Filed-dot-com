from django.contrib import admin

# Register your models here.
from .models import Songs, AudioFile, Podcast
admin.site.register(Songs)
admin.site.register(AudioFile)
admin.site.register(Podcast)