from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import redirect

from wordsplay.game import game_manager as gm


@login_required
def home(request, *args, **kwargs):
    return render(request, 'index.html')


@login_required
def test(request, *args, **kwargs):
    return render(request, 'test.html')


@login_required
def user_profile(request):
    return render(request, 'users/user_profile.html')


def games_requests(request):
    games_requests = gm.get_game_requests(request.user)
    context = RequestContext(request, {
        'game_requests': games_requests.values(),
        'move_time_cases': gm.move_time_cases
    })
    return render(request, 'game/games.html', context)


def games_action(request):
    if request.GET.get('action') == 'cencel':
        gm.cencel_game_request(request.user)
    if request.GET.get('action') == 'create':
        move_time = request.GET.get('move_time')
        gm.create_game_request(request.user, move_time)
    return redirect('ring')
