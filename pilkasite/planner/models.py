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
        """Returns the URL to access a particular instance of the model."""
        return reverse('player-detail', args=[str(self.id)])

class Game(models.Model):
    date = models.DateField()
    notes = models.TextField(max_length=2000)

    def __str__(self):
        return f'game at {self.date}'


    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('game-detail', args=[str(self.id)])


class Squad(models.Model):
    is_player_white = models.BooleanField()
    notes = models.TextField(max_length=1000, blank=True, default='')
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'player {self.player.username} played on {self.game.date} white={self.is_player_white}'


    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('squad-detail', args=[str(self.id)])
