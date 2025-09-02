from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from videos.models import Video


def index(request):
    return render(request, 'videos/index.html')

def video_stream(request, filename):
    ...

class CreateVideo(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'videos/create_video.html'


    def get_success_url(self):
        return reverse('video-details', kwargs={'pk': self.object.pk})


class DetailVideo(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'videos/video_detail.html'


class UpdateVideo(LoginRequiredMixin, UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse('video-details', kwargs={'pk': self.object.pk})


class DeleteVideo(LoginRequiredMixin, DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        return reverse('index')