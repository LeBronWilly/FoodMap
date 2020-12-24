from django.contrib import admin
from areas.models import Country
from areas.models import City

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'last_modify_date', 'created')

class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country_id', 'last_modify_date',"created")

# Register your models here.

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)

