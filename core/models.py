from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    code_confirm = models.CharField(max_length=100, default='')
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.email


class Course(models.Model):
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class Module(models.Model):
    description = models.CharField(max_length=100)
    course = models.ManyToManyField(Course)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class Class(models.Model):
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=800)
    module = models.ForeignKey(Module)

    def __str__(self):
        return self.description


class Member(models.Model):
    user = models.ForeignKey(User)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.username
