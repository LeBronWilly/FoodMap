from django.contrib import admin
from DBMgr.models import Company
from DBMgr.models import ConvenienceStore
from DBMgr.models import show
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','jobname','jobaddress')
class ConvenienceStoreAdmin(admin.ModelAdmin):
    list_display = ('id','convenience_class','convenience_name','convenience_address')
class showAdmin(admin.ModelAdmin):
    list_display = ('id','title','location','locationName','latitude','longitude')

admin.site.register(Company,CompanyAdmin)
admin.site.register(ConvenienceStore,ConvenienceStoreAdmin)
admin.site.register(show,showAdmin)
