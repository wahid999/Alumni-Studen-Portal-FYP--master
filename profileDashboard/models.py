from django.contrib.auth import get_user_model
from django.db import models
User=get_user_model()
POST_TYPE_CHOICES=[('Student Alumni','Student Alumni'),('Professional Alumni','Professional Alumni')]
DEGREE_TIME_SESSION=[('two','2'),('four','4')]

from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

class Profile(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    alumniType = models.CharField(max_length=30, choices=POST_TYPE_CHOICES)
    profilePic = models.ImageField(null=True, upload_to='Profile (User)',default="Profile (User)/user-logo.jpg") 
    
    intro = models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Degree(models.Model):
    name = models.CharField(max_length=50)
    timeSession = models.CharField(max_length=30, choices=DEGREE_TIME_SESSION)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    
class UserDegree(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dateStarted = models.IntegerField()
    dateFinished = models.IntegerField()
    def __str__(self):
        return self.user.username  
  
class WorkExperience(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)
    experienceTime = models.CharField(max_length=20)
    position = models.CharField(max_length=60,null=True)
    portfolioWebsite = models.CharField(max_length=50, null=True)

    

    