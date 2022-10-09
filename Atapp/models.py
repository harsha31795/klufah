from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Book(models.Model):
    GENDER=[('Male','Male'),('Female','Female'),('Others','Others')]
    ACNONAC=[('Ac','Ac'),('Non-Ac','Non-Ac')]
    MUSIC=[('Yes','Yes'),('No','No'),]
    STATUS=[('Pending','Pending'),('Approved','Approved'),('Paid','Paid')]
    dashuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'Dashuser',default="")
    name=models.CharField(max_length=50,default='null')
    email=models.EmailField()
    age=models.IntegerField(default=0)
    phone=models.CharField(default=0,max_length=15)
    gender=models.CharField(max_length=7,choices=GENDER,default='others')
    state=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    event=models.CharField(max_length=25)
    venues=models.CharField(max_length=25)
    acnonac=models.CharField(max_length=10,choices=ACNONAC,default='AC')
    music=models.CharField(max_length=5,choices=MUSIC,default='YES')
    decorations=models.CharField(max_length=50,default='null')
    estimation=models.IntegerField(default=0)
    food=models.CharField(max_length=12,default='null')
    plate=models.CharField(max_length=30,default='null')
    doe=models.DateField(default=date.today)
    status = models.CharField(max_length=20,choices=STATUS,default="Pending")


    def __str__(self):
        return f'{self.dashuser} Booking'

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title

class Profile(models.Model):
    profileuser = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'Profile')
    phone=models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/', default='default.svg')
    def __str__(self):
        return f'{self.profileuser} Profile'

