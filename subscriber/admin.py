from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Subscriber, NextOfKin
from simRegistration.admin import SimRegistrationInline


# Register your models here.
class NextOfKinInline(admin.StackedInline):
    model = NextOfKin


class SubscriberAdmin(UserAdmin):
    inlines = [NextOfKinInline, SimRegistrationInline]

    fieldsets = UserAdmin.fieldsets + (
        ('More personal info', {'fields': ('gender',
                                           'date_of_birth',
                                           'state_of_origin',
                                           'occupation',
                                           'address',
                                           'local_government',
                                           'nationality',
                                           'image',
                                           'role')}),
    )


admin.site.register(Subscriber, SubscriberAdmin)
