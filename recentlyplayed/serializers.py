from rest_framework import serializers
from .models import RecentlyPlayed

class RecentlyPlayedSerializer(serializers.ModelSerializer):
    song_id = serializers.IntegerField(source='song.id', read_only=True)
    song_title = serializers.CharField(source='song.title', read_only=True)
    song_artist = serializers.CharField(source='song.artist.name', read_only=True)
    song_image = serializers.ImageField(source='song.image', read_only=True)
    song_track = serializers.FileField(source='song.track', read_only=True)

    class Meta:
        model = RecentlyPlayed
        fields = [
            'id',
            'song_id',
            'song_title',
            'song_artist',
            'song_image',
            'song_track',
            'played_at',
        ]
