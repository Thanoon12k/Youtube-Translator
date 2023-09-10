from django.shortcuts import render
from .video2audio import videoToAudio
import os


def home(request):
    result = "waiting to upload video"
    if request.method == 'POST' and 'video' in request.FILES:
        video_file = request.FILES['video']
        result = videoToAudio(video_file)
       

    return render(request, 'video2audio.html', {'result': result})