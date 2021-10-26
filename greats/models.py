from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)
    years_active = models.CharField(max_length=16)
    bio = models.TextField(max_length=1600)

    def __str__(self):
        return self.name