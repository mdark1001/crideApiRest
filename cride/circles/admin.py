from django.contrib import admin

# Register your models here.
from .models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_verified', 'is_public', 'rides_taken', 'rides_offered']
    list_filter = ['created', 'is_verified', 'is_public','is_limited']
