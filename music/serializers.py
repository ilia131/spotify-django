from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()

    class Meta :
        model = Songs
        fields = '__all__'
    
    
    def get_artist_name(self, obj):
        return obj.artist.artistname