from rest_framework import serializers
from .models import Artist
from music.models import Songs
from music.serializers import SongSerializer

class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'
        

    def user_songs(self, artist):
        posts = Songs.objects.filter(artist=artist)
        return SongSerializer(posts, many=True).data


        
        