from django.test import TestCase
from ..models import Movie

class URLTests(TestCase):
    def setUp(self):
        Movie.objects.create(title_en="movie 1")

    def test_get_one(self):
        response = self.client.get('/vod_api/movies/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 200)
        self.assertEqual(response.json().get('data').get('id'), 1)