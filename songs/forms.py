from datetime import date

from django import forms

from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'lyrics', 'release_date', 'is_published']
        labels = {
            'title': 'Title of the Song',
            'is_published': 'Should this song be in the portal?',
        }
        widgets = {
            'lyrics': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'release_date': forms.SelectDateWidget(
                years=range(1900, date.today().year + 1)
            ),
        }
