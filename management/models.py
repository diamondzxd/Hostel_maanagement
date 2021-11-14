from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=10, unique=True, blank=True)
    course = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.TextField(max_length=250)


class Room(models.Model):
    category = models.CharField(max_length=50)
    rent = models.IntegerField()
    student = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='student')


class Payment(models.Model):
    payment_mode = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

