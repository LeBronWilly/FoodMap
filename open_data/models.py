# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from areas.models import Country
from areas.models import City
from TeamWork2 import settings
from django.utils import timezone



# class Company(models.Model):
#     jobname = models.TextField(db_column='jobName', blank=True, null=True)  # Field name made lowercase.
#     jobaddress = models.TextField(db_column='jobAddress', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'company'
#
#
# class ConvenienceStore(models.Model):
#     convenience_class = models.TextField(blank=True, null=True)
#     convenience_name = models.TextField(blank=True, null=True)
#     convenience_address = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'convenienceStore'
#
#
# class show(models.Model):
#     title = models.TextField()
#     location = models.TextField()
#     locationName = models.TextField()
#
#     class Meta:
#         managed = True
#         db_table = "show"

class restaurant(models.Model):
    restaurant_name = models.TextField()
    restaurant_address = models.TextField()
    country = models.ForeignKey(Country, on_delete='models.CASCADE', default=1)
    city = models.ForeignKey(City, on_delete='models.CASCADE', default=1)

    def __str__(self):
        return self.restaurant_name
    class Meta:
        managed = True
        db_table = "restaurant"


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


