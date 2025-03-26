
# Create your models here.
from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)
    major = models.IntegerField(unique=True)  # Maps to beacon Major

    def __str__(self):
        return self.name

class Promotion(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.content} ({self.area})"