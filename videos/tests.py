from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from .models import Video
from netflix.db.models import PublishStateOptions


class VideoModelTestCase(TestCase):
    def setUp(self) -> None:
        self.vid1 = Video.objects.create(title='Test title', video_id='1')
        self.vid2 = Video.objects.create(title='Test title', video_id='2', state=PublishStateOptions.PUBLISH)

    def test_created_count(self):
        qs = Video.objects.all()

        self.assertEqual(qs.count(), 2)

    def test_valid_title(self):
        title = 'Test title'
        qs = Video.objects.filter(title=title)

        self.assertTrue(qs.exists())

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)

        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)

        self.assertEqual(qs.count(), 1)

    def test_timestamp(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        timestamps_qs = Video.objects.filter(puplish_timestamp__lte=now)

        self.assertTrue(timestamps_qs.exists())

    def test_slug_field(self):
        title = self.vid1.title
        test_slug = slugify(title)

        self.assertEqual(test_slug, self.vid1.slug)