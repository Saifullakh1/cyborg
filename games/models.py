from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    image = models.FileField(upload_to="game_images")
    rating = models.FloatField(default=5.0)
    downloads = models.FloatField(default=0)

    def __str__(self):
        return self.title