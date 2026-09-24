from django.http import HttpResponse
from django.shortcuts import render


def song_list(request):
    songs = [
        {"id": 1, "title": "Song 1", "artist": "Artist 1"},
        {"id": 2, "title": "Song 2", "artist": "Artist 2"},
        {"id": 3, "title": "Song 3", "artist": "Artist 3"},
    ]
    return render(request, "songs/song_list.html", {"songs": songs} )


def song_detail(request, song_id):
    return HttpResponse(f"Details of song with ID: {song_id}")
