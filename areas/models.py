from django.db import models

# Create your models here.

class Country(models.Model):
    # id = models.IntegerField(primary_key=True)
    country_name = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "country"

class City(models.Model):
    city_name = models.TextField()
    # country_id = models.ForeignKey(Country, on_delete='models.CASCADE', default=1)
    country_id = models.IntegerField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "city"