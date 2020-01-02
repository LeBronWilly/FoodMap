from django.contrib import admin
from open_data.models import Company
from open_data.models import ConvenienceStore
from open_data.models import show



# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobname', 'jobaddress')


class ConvenienceStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'convenience_class', 'convenience_name', 'convenience_address',)


class ShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'locationName',)




admin.site.register(Company, CompanyAdmin)
admin.site.register(ConvenienceStore, ConvenienceStoreAdmin)
admin.site.register(show, ShowAdmin)

