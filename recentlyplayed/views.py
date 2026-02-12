from rest_framework import generics, permissions
from .models import RecentlyPlayed
from .serializers import RecentlyPlayedSerializer

class RecentlyPlayedList(generics.ListAPIView):
    serializer_class = RecentlyPlayedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RecentlyPlayed.objects.filter(user=self.request.user)[:20]  
