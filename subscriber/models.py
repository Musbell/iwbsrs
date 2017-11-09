from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
USER_TYPE = (('SUBSCRIBER','SUBSCRIBER'),('REGISTRATION AGENT','REGISTRATION AGENT'),
             ('MOBILE NETWORK OPERATOR','MOBILE NETWORK OPERATOR'))

GENDER_TYPE = (('MALE','MALE'),('FEMALE','FEMALE'))

RELATION_TYPE = (
    ('FATHER','FATHER'),('MOTHER','MOTHER'),('BROTHER','BROTHER'),('SISTER','SISTER'),('UNCLE','UNCLE'),('AUNT','AUNT'))


class Subscriber(AbstractUser):
    gender = models.CharField(max_length=10,null=True,choices=GENDER_TYPE)
    date_of_birth = models.DateField(null=True,blank=True)
    state_of_origin = models.CharField(max_length=30,null=True)
    occupation = models.CharField(max_length=250,null=True)
    address = models.TextField(default='Address')
    local_government = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    width = models.IntegerField(default=300)
    height = models.IntegerField(default=300)
    image = models.FileField(verbose_name='Captured image', width_field='width', height_field='height',)
    # image = models.FileField(verbose_name='Captured image')
    role = models.CharField(max_length=30,choices=USER_TYPE,default='SUBSCRIBER')


class NextOfKin(models.Model):
    referrer = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    relationship = models.CharField(max_length=10,choices=RELATION_TYPE)
    address = models.TextField(default='Address')
    phone_number = models.CharField(max_length=11)


class CaptureImage(models.Model):
    identity = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    model_pic = models.FileField(upload_to='media/', default='media/None/no-img.jpg')
