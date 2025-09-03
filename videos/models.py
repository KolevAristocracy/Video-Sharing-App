from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


UserModel = get_user_model()


class Video(models.Model):
    uploader = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(
        upload_to='uploads/video_files',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4']),
        ])
    thumbnail = models.FileField(
        upload_to='uploads/thumbnails',
        validators=[
            FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])
        ]
    )
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def delete(self, using = None, keep_parents = False):
        # Delete the file from storage
        if self.video_file:
            self.video_file.delete(save=False)

        if self.thumbnail:
            self.thumbnail.delete(save=False)

        super().delete(using, keep_parents)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user} | Created On: {self.created_on.strftime('%b %d %Y %I:%M %p')}"


