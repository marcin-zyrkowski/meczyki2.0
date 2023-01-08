from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player, Game, Squad


@login_required
def index(request):
    num_players = Player.objects.all().count()
    num_games = Game.objects.all().count()
    context = {
        'num_players': num_players,
        'num_games': num_games,
    }

    return render(request, 'index.html', context=context)


class PlayerListView(LoginRequiredMixin, generic.ListView):
    model = Player


class PlayerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Player


class GameListView(LoginRequiredMixin, generic.ListView):
    model = Game


class GameDetailView(LoginRequiredMixin, generic.DetailView):
    model = Game
