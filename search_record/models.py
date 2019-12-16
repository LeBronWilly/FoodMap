from django.db import models
from django.utils import timezone
# Create your models here.


class SearchRecord(models.Model):
    user_id = models.IntegerField(max_length=200)
    address = models.TextField()
    range = models.IntegerField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'search_record'


