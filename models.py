from django.db import models
from django.contrib.auth.models import User

class StudentDetails(models.Model):
    Student_Name = models.CharField(max_length=25)
    Student_Id = models.CharField(max_length=25,unique=True)
    Password = models.CharField(max_length=25)
    Confirm_PassWord = models.CharField(max_length=25)
    Email_ID = models.EmailField(unique=True)
    Contact_No = models.IntegerField(unique=True)
    Password_Key = models.CharField(max_length=25)

    def __str__(self):
        return self.Student_Id

class AdminDetails(models.Model):
    Admin_Name = models.CharField(max_length=25)
    Admin_Id = models.CharField(max_length=25,unique=True)
    Password = models.CharField(max_length=25)
    Confirm_PassWord = models.CharField(max_length=25)
    Email_ID = models.EmailField(unique=True)
    Contact_No = models.IntegerField(unique=True)
    Password_Key = models.CharField(max_length=25)

    def __str__(self):
        return self.Admin_Id
