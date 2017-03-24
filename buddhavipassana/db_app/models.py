from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class Meditator(models.Model):
    name = models.CharField(max_length=264)
    country = models.CharField(max_length=120)
    born = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=60, unique=True)
    phone = models.CharField(max_length=60)
    profession = models.CharField(max_length=60)
    course = models.CharField(max_length=60)
    course_date = models.DateField()
    teacher = models.CharField(max_length=60)
    remarks = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


