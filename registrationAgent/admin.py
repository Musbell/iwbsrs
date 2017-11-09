from django.contrib import admin
from .models import RegistrationAgent


# Register your models here.
class RegistrationAgentAdmin(admin.ModelAdmin):
    list_display = ('agent', 'region', 'state')
    list_filter = ('region', 'state')
    search_fields = ['agent', 'region', 'state']


admin.site.register(RegistrationAgent, RegistrationAgentAdmin)
