from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import SuperHero
from django.urls import reverse


def index(request):
    all_mysuperheroes = SuperHero.objects.all()
    context = {
        'all_mysuperheroes': all_mysuperheroes
    }
    return render(request, 'mysuperheroes/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter')
        primary_ability = request.POST.get('primary')
        secondary_ability = request.POST.get('secondary')
        catch_phrase = request.POST.get('phrase')
        new_superhero = SuperHero(name=name, alter_ego=alter_ego, primary_ability=primary_ability,
                                  secondary_ability=secondary_ability, catch_phrase=catch_phrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('mysuperheroes:index'))
    else:
        return render(request, 'mysuperheroes/create.html')


def detail():
    return None
