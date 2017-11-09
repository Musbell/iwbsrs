from django.contrib import admin
from .models import RegisteredSims

class SimRegistrationInline(admin.TabularInline):
    model = RegisteredSims