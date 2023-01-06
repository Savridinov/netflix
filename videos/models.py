from django.db import models
from .managers import VideoManager


class Video(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    # timestamp
    # updated
    # state
    # puplish_timestamp

    class Meta:
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'

    def is_published(self):
        return self.active


class VideoProxy(Video):
    objects = VideoManager()

    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'
