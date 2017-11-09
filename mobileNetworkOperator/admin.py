from django.contrib import admin
from .models import MobileNetworkOperator


# Register your models here.
class MobileNetworkOperatorAdmin(admin.ModelAdmin):
    list_display = ('operator', 'mobile_network')
    list_filter = ('mobile_network',)
    search_fields = ['operator', 'mobile_network']


admin.site.register(MobileNetworkOperator, MobileNetworkOperatorAdmin)
