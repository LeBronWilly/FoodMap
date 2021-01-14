from django.contrib import admin
from open_data.models import restaurant
# from open_data.models import ConvenienceStore
# from open_data.models import show



# Register your models here

class restaurantAdmin(admin.ModelAdmin):
    list_display = ("id", 'country',"city",'restaurant_name', 'restaurant_address')
    list_filter = ['country']
    fields = ['restaurant_name', 'restaurant_address']

# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('country_name', 'last_modify_date', 'created')

# class CityAdmin(admin.ModelAdmin):
#     list_display = ('city_name', 'country_id', 'last_modify_date',"created")


# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'jobname', 'jobaddress')
#
#
# class ConvenienceStoreAdmin(admin.ModelAdmin):
#     list_display = ('id', 'convenience_class', 'convenience_name', 'convenience_address',)
#
#
# class ShowAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'location', 'locationName',)



admin.site.register(restaurant, restaurantAdmin)
# admin.site.register(Country, CountryAdmin)
# admin.site.register(City, CityAdmin)

# admin.site.register(Company, CompanyAdmin)
# admin.site.register(ConvenienceStore, ConvenienceStoreAdmin)
# admin.site.register(show, ShowAdmin)

