# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from TeamWork2 import settings
from django.utils import timezone



class Company(models.Model):
    jobname = models.TextField(db_column='jobName', blank=True, null=True)  # Field name made lowercase.
    jobaddress = models.TextField(db_column='jobAddress', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'company'


class ConvenienceStore(models.Model):
    convenience_class = models.TextField(blank=True, null=True)
    convenience_name = models.TextField(blank=True, null=True)
    convenience_address = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'convenienceStore'


class show(models.Model):
    title = models.TextField()
    location = models.TextField()
    locationName = models.TextField()

    class Meta:
        managed = True
        db_table = "show"

# import json
#
# input_file = open('SearchShowAction.json',encoding="utf-8")
# json_array = json.load(input_file)
# count = 0
# for item in json_array:
#     title = item['title']
#     for info in item['showInfo']:
#         location = info['location']
#         locationName = info['locationName']
#         show.objects.create(title=title, location=location, locationName=locationName,)


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