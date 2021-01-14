from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["id","password","last_login","is_superuser","username", 'email',"date_joined"]

# user_id
# password
# last_login
# is_superuser
# username
# first_name
# last_name
# email
# date_jioned

admin.site.register(CustomUser, CustomUserAdmin)