from django.urls import path
from profiles.views import ProfileView, UpdateProfile

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', UpdateProfile.as_view(), name='update_profile'),
]