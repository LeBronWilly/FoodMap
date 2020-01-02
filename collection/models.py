from TeamWork2 import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from open_data.models import show,ConvenienceStore,Company

class favoriteshow(models.Model):
    favorite = models.ForeignKey(show, related_name='show_related', on_delete=models.CASCADE, default=1)
    favorite_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    time = models.DateTimeField(default=timezone.now)


class favoritecompany(models.Model):
    favorite = models.ForeignKey(Company, related_name='company_related', on_delete=models.CASCADE, default=1)
    favorite_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    time = models.DateTimeField(default=timezone.now)


class favoritestore(models.Model):
    favorite = models.ForeignKey(ConvenienceStore, related_name='store_related', on_delete=models.CASCADE, default=1)
    favorite_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    time = models.DateTimeField(default=timezone.now)