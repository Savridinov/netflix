from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify
from netflix.db.models import PublishStateOptions
from .models import Playlist
from videos.models import Video


class PlaylistsModelTestCase(TestCase):
    def setUp(self) -> None:
        vid1 = Video.objects.create(title='Video 1', video_id='abc')
        self.vid1 = vid1
        self.ply1 = Playlist.objects.create(title='Test title')
        self.ply2 = Playlist.objects.create(title='Test title', state=PublishStateOptions.PUBLISH)

    def test_created_count(self):
        qs = Playlist.objects.all()

        self.assertEqual(qs.count(), 2)

    def test_valid_title(self):
        title = 'Test title'
        qs = Playlist.objects.filter(title=title)

        self.assertTrue(qs.exists())

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)

        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)

        self.assertEqual(qs.count(), 1)

    def test_timestamp(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        timestamps_qs = Playlist.objects.filter(puplish_timestamp__lte=now)

        self.assertTrue(timestamps_qs.exists())

    def test_slug_field(self):
        title = self.ply1.title
        test_slug = slugify(title)

        self.assertEqual(test_slug, self.ply1.slug)