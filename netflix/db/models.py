from django.db import models


class PublishStateOptions(models.TextChoices):
    # CONSTANT = db_value, user dislpay value
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'