from django.db import models
from tasks.models import Project, Task
# Create your models here.
class BugReport(models.Model):
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]

    PRIORITY_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    project = models.ForeignKey(
        Project,
        related_name='bug_report',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bug_report',
        on_delete=models.SET_NULL,
        null=True
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Сonsideration'
    )

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]

    PRIORITY_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    project = models.ForeignKey(
        Project,
        related_name='feature_request',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_request',
        on_delete=models.SET_NULL,
        null=True
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Сonsideration'
    )

    def __str__(self):
        return self.title

