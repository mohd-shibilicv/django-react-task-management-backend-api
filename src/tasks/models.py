from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', "Pending"),
        ('in_progress', "In Progress"),
        ('completed', "Completed"),
    ]
    PRIORITY_STATUS = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    priority = models.CharField(max_length=20, choices=PRIORITY_STATUS, default="medium")
    due_date = models.DateField()

    def clean(self):
        if not self.title:
            raise ValidationError("Title cannot be empty.")
        if self.due_date <= timezone.now():
            raise ValidationError("Due date must be in the future.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
