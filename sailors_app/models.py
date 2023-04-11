from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Sailor(AbstractUser):
    position = models.ForeignKey(
        to=Position,
        on_delete=models.SET_NULL,
        null=True,
        default="Simple sailor"
    )

    def __str__(self):
        return f"{self.username} ({self.position})"


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    PRIORITY_LEVEL = (
        ("low", "LOW"),
        ("middle", "MIDDLE"),
        ("high", "HIGH"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    deadline = models.DateField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVEL)
    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Sailor, related_name="sailors")

    def __str__(self):
        return f"{self.name}"
