from django.test import TestCase
from ..models import Series

class URLTests(TestCase):
    def setUp(self):
        Series.objects.create(title_en="series 1")

    def test_get_one(self):
        response = self.client.get('/vod_api/series/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 200)
        self.assertEqual(response.json().get('data').get('id'), 1)