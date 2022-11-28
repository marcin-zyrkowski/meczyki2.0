from django.shortcuts import render
from django.views import generic
from .models import Player, Game, Squad

def index(request):
    num_players = Player.objects.all().count()
    num_games = Game.objects.all().count()
    context = {
        'num_players' : num_players,
        'num_games' : num_games,
    }

    return render(request, 'index.html', context=context)

class PlayerListView(generic.ListView):
    model = Player

class PlayerDetailView(generic.DetailView):
    model = Player

class GameListView(generic.ListView):
    model = Game