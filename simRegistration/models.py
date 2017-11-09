from django.conf import settings
from django.db import models
from mobileNetworks.models import MobileNetworks


# Create your models here.
class RegisteredSims(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=11, unique=True,)
    mobile_network = models.ForeignKey(MobileNetworks, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Registered sim'
        verbose_name_plural = 'Registered sims'
        unique_together = ("owner", "phone_number")


