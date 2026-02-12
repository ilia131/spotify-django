from rest_framework import generics, permissions
from .models import Songs
from .serializers import SongSerializer
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import mark_as_played
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions


class SongAPIView(generics.GenericAPIView,
                  generics.mixins.ListModelMixin,
                  generics.mixins.CreateModelMixin,
                  generics.mixins.RetrieveModelMixin,
                  generics.mixins.UpdateModelMixin,
                  generics.mixins.DestroyModelMixin):
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Songs.objects.filter(artist=self.request.user)

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)









class PlaySongAPIView(APIView):
    

    def post(self, request, song_id):
        song = get_object_or_404(Songs, id=song_id)

        mark_as_played(request.user, song)

        return Response({"status": "ok"}, status=status.HTTP_200_OK)
