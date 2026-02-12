from rest_framework import serializers
from .models import View

       
       
class ViewSerlizers(serializers.ModelSerializer):
     total_views = serializers.IntegerField(read_only=True)
     authorview = serializers.CharField(source='authorview.artistname', read_only=True)
     postview = serializers.CharField(source='postview.unique_id')
     views_count = serializers.IntegerField(default=0)
     class Meta:
        model = View
        fields = ('id' , 'views_count'  , 'postview' , 'authorview' , 'total_views')  