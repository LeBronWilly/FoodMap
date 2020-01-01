from django.contrib import admin
from DBMgr.models import Company
from DBMgr.models import ConvenienceStore
from DBMgr.models import show
from DBMgr.models import favoritecompany,favoriteshow,favoritestore


# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobname', 'jobaddress')


class ConvenienceStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'convenience_class', 'convenience_name', 'convenience_address',)


class ShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'locationName',)

class favoritecompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'favorite', 'favorite_user', 'time',)

class favoriteshowAdmin(admin.ModelAdmin):
    list_display = ('id', 'favorite', 'favorite_user', 'time',)

class favoritestoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'favorite', 'favorite_user', 'time',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(ConvenienceStore, ConvenienceStoreAdmin)
admin.site.register(show, ShowAdmin)
admin.site.register(favoritecompany, favoritecompanyAdmin)
admin.site.register(favoriteshow, favoriteshowAdmin)
admin.site.register(favoritestore, favoritestoreAdmin)
