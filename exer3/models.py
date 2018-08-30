from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    Student_Name = models.ForeignKey(Student, on_delete=models.CASCADE)
    Class_Section = models.ForeignKey(Section, on_delete=models.CASCADE)