from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=256)
    years_active = models.CharField(max_length=16)
    bio = models.TextField(max_length=1600)

    def __str__(self):
        return self.name

class Review(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=24)
    subject = models.CharField(max_length=32)
    body = models.TextField(max_length=4000)

    def __str__(self):
        return self.subject