from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100, blank=True, null=True)
    audio_url = models.CharField(max_length=100)
    duration = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title
