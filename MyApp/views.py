from django.http import HttpResponse
from django.shortcuts import render

import requests

from MyApp.classes.Team import Team
from MyApp.classes.pokemon import Pokemon


# Create your views here.

def index(request):
    listPokemonRequest = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=1000").json()['results']
    listPokemon = Pokemon.objects.values()
    if listPokemon.count() < 200:
        for pokemonUrlRequest in listPokemonRequest:
            pokemonRequest = requests.get(pokemonUrlRequest['url']).json()
            types = ""
            print(pokemonRequest['sprites']['front_default'])
            for type in pokemonRequest['types']:
                types += ' ' + type['type']['name']
            tmpPokemon = Pokemon(name=pokemonRequest['name'],
                                 link_img=pokemonRequest['sprites']['front_default'],
                                 types=types, height=pokemonRequest['height'],
                                 weight=pokemonRequest['weight'],
                                 link_detail=pokemonUrlRequest['url'])
            tmpPokemon.save_base()
    context = {'list_pokemon': listPokemon}
    return render(request, 'myApp/indexPage.html', context)


def pokemonProfil(request, name):
    pokemon = Pokemon.objects.get(name=name)
    pokemon.height /= 10
    pokemon.weight /= 10
    context = {'pokemon': pokemon}
    return render(request, 'myApp/pokemonProfil.html', context)


def equipeProfil(request):
    context = {'team': Team.objects.get(name="team1")}
    return render(request, 'myApp/equipeProfile.html', context)


def equipeAddPokemon(request, name):
    pokemon = Pokemon.objects.get(name=name)
    teamPokemon = Team.objects.get(name="team1")
    if teamPokemon.pokemons.count() < 6:
        teamPokemon.pokemons.add(pokemon)
    teamPokemon.save_base()
    return HttpResponse(index(request))
