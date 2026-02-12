from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from .models import Artist
from .serializers import ArtistSerializer
from music.models import Songs
from music.serializers import SongSerializer


class ArtistAPIView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = [IsAuthenticated]

class ArtistDetailAPIView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]


class MyArtistProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_songs(self, artist):
        posts = Songs.objects.filter(artist=artist)
        return SongSerializer(posts, many=True).data

    def get(self, request):
        try:
            artist = Artist.objects.get(email=request.user.email)

        except Artist.DoesNotExist:
            return Response(
                {"detail": "Artist profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ArtistSerializer(artist)
        data = serializer.data
        data['songs'] = self.get_user_songs(request.user)
        return Response(data)
    



class FeaturedArtistAPIView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = ArtistSerializer
    def get_queryset(self):
        return Artist.objects.filter(is_featured=True)
    
    


        
