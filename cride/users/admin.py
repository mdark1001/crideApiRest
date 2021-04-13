from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone_number']
    list_filter = ['is_active', 'is_staff', 'created']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'rides_token', 'rides_offered', 'reputacion']
    list_filter = ['reputacion']


admin.site.register(User, CustomUserAdmin)
