from django.urls import path
from .views import SongAPIView , PlaySongAPIView

urlpatterns = [
    path('songs/', SongAPIView.as_view()),          
    path('songs/<int:pk>/', SongAPIView.as_view()),
    path('songs/<int:song_id>/play/', PlaySongAPIView.as_view(), name='play-song'),

]