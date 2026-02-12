# apps/songs/services.py
from django.utils import timezone
from .models import  Songs

from recentlyplayed.models import RecentlyPlayed
from django.conf import settings

from django.contrib.auth.models import AnonymousUser
from django.utils import timezone

def mark_as_played(user, song):
    if not user or user.is_anonymous:
        return None 

    obj, created = RecentlyPlayed.objects.update_or_create(
        user=user,
        song=song,
        defaults={'played_at': timezone.now()}
    )
    return obj
