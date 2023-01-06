from django.utils import timezone
from django.utils.text import slugify
from netflix.db.models import PublishStateOptions


def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    if instance.slug is None:
        instance.slug = slugify(title)


def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_published = instance.state == PublishStateOptions.PUBLISH
    is_draft = instance.state == PublishStateOptions.DRAFT
    if is_published and instance.puplish_timestamp is None:
        print('Save as timestamp for published')
        instance.puplish_timestamp = timezone.now()
    elif is_draft:
        instance.puplish_timestamp = None