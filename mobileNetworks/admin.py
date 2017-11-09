from django.contrib import admin
from .models import MobileNetworks


# Register your models here.
class MobileNetworksAdmin(admin.ModelAdmin):
    list_display = ('network_name', 'website')

admin.site.register(MobileNetworks, MobileNetworksAdmin)
