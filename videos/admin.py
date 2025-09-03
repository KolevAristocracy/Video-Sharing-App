from django.contrib import admin

from videos.models import Video, Category


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


