from django.db import models


class Music(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField(blank=True, null=True)
    audio = models.FileField()
    duration = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title
