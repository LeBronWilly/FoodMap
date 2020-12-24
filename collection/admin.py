from django.contrib import admin
from collection.models import favorite_restaurant
# from collection.models import favoritecompany,favoriteshow,favoritestore


class favorite_restaurantAdmin(admin.ModelAdmin):
    list_display = ('favorite', 'favorite_user', 'time')
    list_filter = ['favorite_user']

# class favoritecompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'favorite', 'favorite_user', 'time',)
#
# class favoriteshowAdmin(admin.ModelAdmin):
#     list_display = ('id', 'favorite', 'favorite_user', 'time',)
#
# class favoritestoreAdmin(admin.ModelAdmin):
#     list_display = ('id', 'favorite', 'favorite_user', 'time',)
#


admin.site.register(favorite_restaurant, favorite_restaurantAdmin)
# admin.site.register(favoritecompany, favoritecompanyAdmin)
# admin.site.register(favoriteshow, favoriteshowAdmin)
# admin.site.register(favoritestore, favoritestoreAdmin)