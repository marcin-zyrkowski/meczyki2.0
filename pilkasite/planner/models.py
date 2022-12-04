from django.db import models
from django.urls import reverse

class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_permanent = models.BooleanField()

    def __str__(self):
        return f'{self.name} {self.surname} aka {self.username}'

    def get_absolute_url(self):
        return reverse('player-detail', args=[str(self.id)])

class Game(models.Model):
    date = models.DateField()
    notes = models.TextField(max_length=2000)

    def __str__(self):
        return f'game at {self.date}'

    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.id)])


class Squad(models.Model):
    is_player_white = models.BooleanField()
    notes = models.TextField(max_length=1000, blank=True, default='')
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    absent_player = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True, blank=True, related_name='absent_player')
    substitution_order = models.SmallIntegerField(default=0)

    def __str__(self):
        kolor = 'czarnych'
        if self.is_player_white:
            kolor = 'białych'

        return f'{self.game.date} grał w {kolor} '


    def get_absolute_url(self):
        return reverse('squad-detail', args=[str(self.id)])
