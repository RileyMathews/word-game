from django.db import models

class Game(models.Model):
    room_code = models.SlugField(max_length=4)
