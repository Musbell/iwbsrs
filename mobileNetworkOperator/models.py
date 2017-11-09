from django.db import models
from mobileNetworks.models import MobileNetworks
from django.conf import settings


# Create your models here.

class MobileNetworkOperator(models.Model):
    operator = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE, )
    mobile_network = models.OneToOneField(MobileNetworks, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Mobile network operator"
        verbose_name_plural = "Mobile network operators"

    def __str__(self):
        return self.operator.username



