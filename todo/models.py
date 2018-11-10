from django.db import models

# Create your models here.
class Todo(models.Model):
    head = models.CharField(max_length=20)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.head
