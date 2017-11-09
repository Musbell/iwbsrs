from django.db import models


# Create your models here.
class MobileNetworks(models.Model):
    network_name = models.CharField(max_length=30)
    website = models.URLField()

    class Meta:
        verbose_name = 'Mobile network'
        verbose_name_plural = 'Mobile networks'

    def __str__(self):
        return self.network_name
