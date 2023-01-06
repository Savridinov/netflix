from django.test import TestCase
from .models import Video


class VideoModelTestCase(TestCase):
    def setUp(self) -> None:
        Video.objects.create(title='Test title')

    def test_created_count(self):
        qs = Video.objects.all()

        self.assertEqual(qs.count(), 1)

    def test_valid_title(self):
        title = 'Test title'
        qs = Video.objects.filter(title=title)

        self.assertTrue(qs.exists())
