from django.db import models

class WordCard(models.Model):
    word = models.CharField()
    board_position = models.IntegerField()

    class CardType(models.TextChoices):
        BASIC = 'BA'
        BLUE = 'BL'
        RED = 'RE'
        POISON = 'PO'

    card_type = models.TextField(choices=CardType)
