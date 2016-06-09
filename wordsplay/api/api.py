import time

from wordsplay.models import Game


def create_game(user1, user2):
    game = Game(user1, user2, time.time(), "started")
    Game.save(game)


def get_games(user):
    return Game.objects.filter(user1=user) + Game.objects.filter(user2=user)
