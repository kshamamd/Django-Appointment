from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class New(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', blank='True')
    surname = models.CharField(max_length=50, default='', blank='True')
    role = models.CharField(max_length=50, default='', blank='True')
    number = models.CharField(max_length=50, default='', blank='True')
    date = models.DateTimeField(default=timezone.now)
    optional_number = models.CharField(max_length=50, default='', blank='True')
    address = models.CharField(max_length=50, default='', blank='True')
    reason = models.CharField(max_length=50, default='', blank='True')
    status = models.BooleanField(default='False')


def __str__(self):
    return f'{self.user.name} New'

#def submit(self):

# Create your models here.CASCADE means that if the user get deleted, delete the profile
# but if we delete the profile it wont delete the user it just a one way thing

