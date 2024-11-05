
from django.db import models
from django import forms

class Student(models.Model):
    # Fields for the Student model

    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, verbose_name="Profile Image URL")
    full_name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_joined = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

class Program(models.Model):
    name = models.CharField(max_length=100, default='Default Program')   # Add appropriate fields
    # Add any other fields necessary for your program

    def __str__(self):
        return self.name

class Student_Profile(models.Model):
    # Fields for the Student_Profile model
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    date_join = models.DateField()
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='student_profile')

class CohortGroup(models.Model):
    # Fields for the CohortGroup model
    name = models.CharField(max_length=100)
    date_join = models.DateField()

 # Add a default value
    # Add any other fields necessary for your program

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name


