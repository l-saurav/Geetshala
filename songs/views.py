from django.http import HttpResponse
from django.shortcuts import render

from .models import Song


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, song_id):
    return HttpResponse(f"Details of song with ID: {song_id}")
