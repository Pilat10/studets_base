from django.db import models

# Create your models here.


class Group(models.Model):
    """

    """
    name = models.CharField(max_length=255)
    headman = models.ForeignKey("Student", related_name='+')


class Student(models.Model):
    """

    """
    fio = models.CharField(max_length=255)
    birthday = models.DateField()
    number_student_cart = models.IntegerField()
    group = models.ForeignKey("Group")