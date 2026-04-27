from django.db import models
from games.models import Game


class Streamer(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.FileField(upload_to="avatars")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Stream(models.Model):
    streamer = models.ForeignKey(Streamer, on_delete=models.CASCADE, related_name="streamers")
    title = models.CharField(max_length=255)
    poster = models.FileField(upload_to="posters")
    views = models.FloatField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="stream_games")

    def __str__(self):
        return self.title
