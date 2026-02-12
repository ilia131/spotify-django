from django.urls import path
from .views import RecentlyPlayedList

urlpatterns = [
    path('recently-played/', RecentlyPlayedList.as_view(), name='recently-played'),
]