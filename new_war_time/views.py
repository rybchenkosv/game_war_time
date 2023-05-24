from django.shortcuts import render, get_object_or_404
from .models import User, Rank, Combat_squad, Experience

def users(request):
    users = get_object_or_404(User)
    rank = get_object_or_404(Rank)

    context = {
        'users': users,
        'rank': rank,
    }

    return render(request, 'base.html' ,context)

def military_personnel(request):
    combat_squad = get_object_or_404(Combat_squad)
    rank = get_object_or_404(Rank)
    experience = get_object_or_404(Experience)

    context = {
        'combat_squad': combat_squad,
        'rank': rank,
        'experience': experience,
    }

    return render(request, 'military_personnel.html', context)

def game(request):
    return render(request, 'game.html')