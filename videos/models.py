from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from .managers import VideoManager


class PublishStateOptions(models.TextChoices):
    # CONSTANT = db_value, user dislpay value
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'


class Video(models.Model):
    VideoStateOptions = PublishStateOptions
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)
    puplish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'

    @property
    def is_published(self):
        return self.active

    def save(self, *args, **kwargs):
        if self.state == self.VideoStateOptions.PUBLISH and self.puplish_timestamp is None:
            print('Save as timestamp for published')
            self.puplish_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.puplish_timestamp = None
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class VideoProxy(Video):
    objects = VideoManager()

    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'
