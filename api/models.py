from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        INSTRUCTOR = 'INSTRUCTOR'
        STUDENT = 'STUDENT'

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.STUDENT
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'ACTIVE'
        COMPLETED = 'COMPLETED'

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    courses = models.ManyToManyField(Course)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE
    )
    class Meta:
        ordering = ['-enrolled_on']

    def __str__(self):
        return f"{self.student} - {self.status}"

class Module(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='modules'
    )
    title = models.CharField(max_length=200)
    duration_minutes = models.IntegerField()

    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.title
