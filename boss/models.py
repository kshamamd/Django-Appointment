from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Appointment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    appoint = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here. appoint is a key


