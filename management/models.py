from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    enrollment = models.CharField(max_length=10, unique=True, blank=True)
    course = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.TextField(max_length=250)

    def __str__(self):
        return '{}{}{}'.format(self.first_name," ", self.enrollment) # returning multiple values


# class Login(models.Model):
#     login_user = models.OneToOneField(Profile, default=None, null=True, on_delete=models.CASCADE)


class Room(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, related_name='student')
    # student = models.ForeignKey(Profile, on_delete=models.PROTECT, default="abc")
    ROOM_CATEGORY = [('single', "SINGLE OCCUPANCY"),
                     ('share', "DOUBLE OCCUPANCY")]
    category = models.CharField(max_length=50, choices=ROOM_CATEGORY, default="choose")

    vacant = models.BooleanField(default=False)
    rent = models.IntegerField()


class Payment(models.Model):
    payment_mode = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Subscription(models.Model):
    starting_date = models.DateField()
    ending_date = models.DateField()
    # student = models.ForeignKey(Profile,on_delete=models.PROTECT,default=1, related_name='student')
    room = models.ForeignKey(Room, on_delete=models.PROTECT,default=1, null=True)

