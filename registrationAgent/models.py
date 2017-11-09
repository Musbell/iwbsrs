from django.db import models
from django.conf import settings


# Create your models here.
class RegistrationAgent(models.Model):
    agent = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,)
    registration_center = models.TextField(default='Registration center')
    region = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = 'Registration agent'
        verbose_name_plural = 'Registration agents'

    def __str__(self):
        return self.agent.username
