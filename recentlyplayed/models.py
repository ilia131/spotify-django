from django.db import models
from django.utils import timezone
from music.models import Songs 
from django.conf import settings

class RecentlyPlayed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recently_played")
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    played_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-played_at']  # جدیدترین‌ها اول
        unique_together = ('user', 'song')  # هر آهنگ یکبار برای هر کاربر

