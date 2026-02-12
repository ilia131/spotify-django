from django.conf import settings
from django.db.models import Sum
from rest_framework import generics , mixins 
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import viewsets , status
from .models import View
from .serializers import ViewSerlizers
from rest_framework.response import Response
from music.models import Songs

     
     
     

class ViewViewSet(viewsets.GenericViewSet, mixins.ListModelMixin , mixins.CreateModelMixin , mixins.DestroyModelMixin):
     permission_classes = [AllowAny]
    #  parser_classes = (MultiPartParser, FormParser)

     queryset = View.objects.all()
     serializer_class = ViewSerlizers
     def get_queryset(self):
         text = self.request.query_params.get('query' , None)
         if not text: 
             return self.queryset
         
         return self.queryset.filter(postview__unique_id=text) 
     
    
     
     def create(self, request, *args, **kwargs):
        user = request.user
        postview_unique_id = request.data.get('postview')  
        
        postview = Songs.objects.get(unique_id=postview_unique_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        queryset_result = self.get_queryset()
        if queryset_result.exists():
            postview_unique_id = queryset_result.first().postview
            
        if View.objects.filter(authorview=user , postview=postview).exists():
           return Response({'error': 'User with artistname cannot create posts'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(authorview=user, postview=postview)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
 
 
     def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)   
     
     
     def delete(self, request, pk):
        instance = self.get_queryset(pk=id)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

     def perform_destroy(self, instance):
         instance.delete()