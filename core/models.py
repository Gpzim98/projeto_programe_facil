import datetime

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
    full_description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class Module(models.Model):
    description = models.CharField(max_length=100)
    full_description = models.TextField()
    course = models.ManyToManyField(Course)
    image = models.CharField(max_length=500)
    order = models.IntegerField(null=True, blank=True)
    slide = models.FileField(upload_to='slides', null=True, blank=True)
    exercise = models.FileField(upload_to='exercises', null=True, blank=True)

    def __str__(self):
        return self.description


class Class(models.Model):
    description = models.CharField(max_length=100)
    full_description = models.TextField()
    link = models.CharField(max_length=800)
    module = models.ForeignKey(Module)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description + ' - ' + self.module.description


class Member(models.Model):
    user = models.ForeignKey(User)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.username


class CourseEnrollment(models.Model):
    member = models.ForeignKey(Member)
    course = models.ForeignKey(Course)
    final_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    final_test = models.FileField(upload_to='tests/final', null=True, blank=True)
    slide = models.FileField(upload_to='slides', null=True, blank=True)

    def __str__(self):
        return self.member.user.username + ' - ' + self.course.description


class ModulesEnrollment(models.Model):
    member = models.ForeignKey(Member)
    module = models.ForeignKey(Module)
    final_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    final_test_answer = models.FileField(upload_to='tests/final', null=True, blank=True)
    date_release = models.DateField()

    @property
    def status(self):
        return False if self.date_release > datetime.date.today() else True

    def __str__(self):
        return self.member.user.username + ' - ' + self.module.description
