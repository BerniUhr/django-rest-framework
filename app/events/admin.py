from django.contrib import admin
from .models import Category
from .models import Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'updated_at']
    list_display_links = ['id', 'name'] # was ist anklickbar?


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'author', 'category', 'is_active']
    list_display_links = ['id', 'name'] # was ist anklickbar?