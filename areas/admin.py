from django.contrib import admin
from areas.models import Country
from areas.models import City

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','country_name', 'last_modify_date', 'created')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','city_name', 'country_id', 'last_modify_date',"created")
    list_filter = ['country_id']

# Register your models here.

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)

