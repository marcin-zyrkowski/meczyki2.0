from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('player/<int:pk>', views.PlayerDetailView.as_view(), name='player-detail'),
]
