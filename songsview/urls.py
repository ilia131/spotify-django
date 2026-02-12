from rest_framework import routers
from . import views
from django.urls import path , include , re_path



router = routers.SimpleRouter()

router.register('view', views.ViewViewSet , basename='view')



urlpatterns = [
    
    path('', include(router.urls))
]
