from django.test import TestCase
from ..models import Season

class Season_Tests(TestCase):
    def setUp(self):
        Season.objects.create(title_en="season 1")

    def test_get_one(self):
        response = self.client.get('/vod_api/seasons/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 200)
        self.assertEqual(response.json().get('data').get('id'), 1)

    def test_get_not_found_one(self):
        response = self.client.get('/vod_api/seasons/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 404)
        self.assertEqual(response.json().get('message'), 'Item Not Found')