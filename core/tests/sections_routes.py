from django.test import TestCase
from ..models import Section

class URLTests(TestCase):
    def setUp(self):
        Section.objects.create(title_en="section 1")

    def test_get_all(self):
        response = self.client.get('/vod_api/sections')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 200)
        self.assertEqual(len(response.json().get('data')), 1)