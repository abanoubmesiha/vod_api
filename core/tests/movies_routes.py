from django.test import TestCase
from ..models import Movie

class Movies_Tests(TestCase):
    def setUp(self):
        Movie.objects.create(title_en="movie 1")

    def test_get_one(self):
        response = self.client.get('/vod_api/movies/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 200)
        self.assertEqual(response.json().get('data').get('id'), 1)

    def test_get_not_found_one(self):
        response = self.client.get('/vod_api/movies/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 404)
        self.assertEqual(response.json().get('message'), 'Item Not Found')