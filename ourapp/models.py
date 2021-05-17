from django.db import models
from datetime import datetime

class School(models.Model):
    name = models.CharField(max_length = 400)

    def __str__(self):
      return self.name

class Certificate_type(models.Model):
    name = models.CharField(max_length = 400)
    
    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length = 400)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 400) 
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length = 50)

    def __str__(self):
        return self.type

class Student(models.Model):
    full_name = models.CharField(max_length = 400)
    year_of_graduation = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Certificate_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name