from django.db import models
from django.conf import settings
import uuid
from django.utils.text import slugify
from django.utils import timezone

class Songs(models.Model):
    # صاحب اصلی آهنگ
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="songs"
    )

    # آرتیست‌های همکاری کرده (optional)
    collaborators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="collaborations"
    )

    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    track = models.FileField(upload_to='music/', blank=True, null=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    slug = models.SlugField(blank=True, null=True, unique=True)
    
    key = models.SlugField(null=True, blank=True)
    ky = models.SlugField(null=True, blank=True)
    
    release_date = models.DateField(default=timezone.now)
    
    play_count = models.PositiveIntegerField(default=0)
    total_listen_time = models.PositiveIntegerField(default=0)
    
    genre = models.CharField(max_length=100, blank=True, null=True)
    
    audio_features = models.JSONField(default=dict, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.artist}'

    def get_image_url(self):
        if self.image:
            return 'https://spotify-django-1.onrender.com/' + self.image.url
        return ''

    def get_track_url(self):
        if self.track:
            return 'https://spotify-django-1.onrender.com/' + self.track.url
        return ''

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def add_play(self, seconds: int = 0):
        self.play_count += 1
        self.total_listen_time += seconds
        self.save(update_fields=['play_count', 'total_listen_time'])
        
    
    def get_artists(self):
        """
        برگرداندن همه آرتیست‌ها: شامل صاحب اصلی و همکاران.
        اگر همکاری نباشه، فقط صاحب اصلی برگردونده میشه.
        """
        artists = [self.artist]
        collaborators = list(self.collaborators.all())
        return artists + collaborators
    
    def __str__(self):
        artist_names = ", ".join([str(a) for a in self.get_artists()])
        return f"{self.title} - {artist_names}"

