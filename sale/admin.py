from django.contrib import admin
from sale.models import MaritalStatus, State, City, Zone


# Register your models here.
@admin.register(MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'created_at', 'modified_at', 'active']


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'created_at', 'modified_at', 'active']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'created_at', 'modified_at', 'active']


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'created_at', 'modified_at', 'active']
