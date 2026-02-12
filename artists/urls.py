from django.urls import path
from .views import ArtistAPIView , MyArtistProfileView , ArtistDetailAPIView , FeaturedArtistAPIView

urlpatterns = [
    path("artists/", ArtistAPIView.as_view()),
    path("artist/<int:pk>/", ArtistDetailAPIView.as_view()),
    path("artist/me/", MyArtistProfileView.as_view()),
    path("artists/featured/", FeaturedArtistAPIView.as_view()),
]
