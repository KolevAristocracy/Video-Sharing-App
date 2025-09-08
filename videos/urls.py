from django.urls import path, include

from videos import views as video_views

urlpatterns = [
    path('', video_views.Index.as_view(), name='index'),
    path('create/', video_views.CreateVideo.as_view(), name='create-video'),
    path('<int:pk>/', video_views.DetailVideo.as_view(), name='video-details'),
    path('<int:pk>/update', video_views.UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', video_views.DeleteVideo.as_view(), name='delete-video'),
    path('category/<int:pk>', video_views.VideoCategoryList.as_view(), name='category-list'),
    path('search/', video_views.SearchVideo.as_view(), name='video-search'),

]