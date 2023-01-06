from django.contrib import admin
from .models import *


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id', 'is_published']
    list_filter = ['active']
    search_fields = ['title']

    class Meta:
        model = Video


class VideoProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id', 'is_published']
    list_filter = ['active']
    search_fields = ['title']

    class Meta:
        model = VideoProxy

    # def get_queryset(self, request):
    #     return VideoProxy.objects.filter(active=True)


admin.site.register(VideoProxy, VideoProxyAdmin)
admin.site.register(Video, VideoAdmin)
