from django.db import models

from django.contrib.auth.models import  AbstractBaseUser , PermissionsMixin
from users.models import UserAccountManager



class Artist(AbstractBaseUser , PermissionsMixin):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255, null=True)
    artistname= models.CharField(max_length=255 , unique=True , blank=True , null=True)
    email = models.EmailField(unique=True , max_length=255)
    bio = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    profile_pic = models.ImageField(
        upload_to='images/',
        null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    background = models.ImageField(
        upload_to='images/',
        null=True)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'artistname']
    
    def get_image(self):
        if self.profile_pic:
            return 'http://127.0.0.1:8000/' + self.profile_pic.url
        return ''
    
    def get_background(self):
         if self.background:
            return 'http://127.0.0.1:8000/' + self.background.url
         return ''
    
   
    def __str__(self):
        return self.email


    # def views_count(self):
        
    #     return View1.objects.filter(views_count=self.pk)
    
    
    
    # def follow_count(self):
    #     return Follow.objects.filter(follow_count=self.pk)
