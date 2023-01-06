from django.db import models
from django.db.models.signals import pre_save
from .managers import VideoManager
from netflix.db.models import PublishStateOptions
from netflix.db.recivers import slugify_pre_save, publish_state_pre_save


class Video(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    puplish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'

    @property
    def is_published(self):
        return self.active


class VideoProxy(Video):
    objects = VideoManager()

    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'


pre_save.connect(slugify_pre_save, sender=Video)
pre_save.connect(publish_state_pre_save, sender=Video)