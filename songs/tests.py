from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Song


class SongModelTests(TestCase):
    def test_string_representation_is_title(self):
        song = Song(title='Phoolko Aankhama Phoolai Sansar', lyrics='...')

        self.assertEqual(str(song), 'Phoolko Aankhama Phoolai Sansar')


class SongViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.published_old = Song.objects.create(
            title='Older published song',
            lyrics='Old lyrics',
            release_date=date(2004, 10, 11),
            is_published=True,
        )
        cls.published_new = Song.objects.create(
            title='Newer published song',
            lyrics='New lyrics',
            release_date=date(2007, 8, 3),
            is_published=True,
        )
        Song.objects.create(
            title='Unpublished song',
            lyrics='Private lyrics',
            release_date=date(2020, 1, 1),
            is_published=False,
        )

    def test_song_list_contains_only_published_songs_newest_first(self):
        response = self.client.get(reverse('songs:song_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context['songs']),
            [self.published_new, self.published_old],
        )
        self.assertNotContains(response, 'Unpublished song')

    def test_song_detail_renders_song(self):
        response = self.client.get(
            reverse('songs:song_detail', args=[self.published_old.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Older published song')
        self.assertContains(response, 'Old lyrics')

    def test_missing_song_detail_returns_not_found(self):
        response = self.client.get(reverse('songs:song_detail', args=[9999]))

        self.assertEqual(response.status_code, 404)

    def test_create_song_form_renders(self):
        response = self.client.get(reverse('songs:create_song'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add New Song Details')
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_create_song_saves_valid_submission_and_redirects(self):
        response = self.client.post(
            reverse('songs:create_song'),
            {
                'title': 'New song',
                'lyrics': 'New lyrics',
                'release_date_year': '2026',
                'release_date_month': '9',
                'release_date_day': '29',
                'is_published': 'on',
            },
        )

        self.assertRedirects(response, reverse('songs:song_list'))
        self.assertTrue(
            Song.objects.filter(title='New song', lyrics='New lyrics').exists()
        )
