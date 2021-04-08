from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView

from .models import SuperHero


def index(request):
    all_mysuperheroes = SuperHero.objects.all()
    context = {
        'all_mysuperheroes': all_mysuperheroes
    }
    return render(request, 'mysuperheroes/index.html', context)


def detail(request):
    superhero = request.get(pk=1)
    context = {
        'single_superhero': superhero
    }
    return render(request, 'single_superhero/detail.html', context)


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


def delete(request):
    mysuperheroes = get_object_or_404(SuperHero, id=id)
    if request.method == 'POST':
        mysuperheroes.delete()
        messages.success(request, "successfully deleted")
        return HttpResponseRedirect("/Blog/list")
