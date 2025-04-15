from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    join_date = models.DateField()
    designation = models.CharField(max_length=100)
    salary = models.FloatField()

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # Present/Absent

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    rating = models.FloatField()
    comments = models.TextField()
