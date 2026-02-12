from django.db import models
from artists.models import Artist
from music.models import Songs
from django.db.models import Sum
from django.conf import settings
from artists.models import Artist

class View(models.Model):
        postview = models.ForeignKey(Songs ,on_delete=models.CASCADE, related_name='postview', null=True , blank=True)
        authorview = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='authorview')
        views_count = models.IntegerField(default=0)

        @property
        def total_views(self):
            total_views_count = View.objects.filter(postview=self.postview).aggregate(total_views=Sum('views_count'))
            total_sum = total_views_count['total_views'] if total_views_count['total_views'] else 0
            
            return total_sum
           
