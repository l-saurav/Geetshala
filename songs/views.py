from django.shortcuts import get_object_or_404, render

from .models import Song


def song_list(request):
    songs = Song.objects.filter(is_published=True).order_by('-release_date')
    return render(request, 'songs/song_list.html', {'songs': songs})


def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'songs/song_detail.html', {'song': song})
