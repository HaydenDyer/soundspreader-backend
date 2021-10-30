from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    author = models.CharField(max_length=24)
    subject = models.CharField(max_length=32)
    body = models.TextField(max_length=800)
    created_on = models.DateField(default=now)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return f'{self.author} - {self.subject}'