from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm

def index(request):
    pokemons = Pokemon.objects.order_by('name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_list(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('trainers.html')
    return HttpResponse(template.render({'trainers': trainers}, request))

def display_trainer(request, id: int):
    trainer = Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
        form = PokemonForm()
            
    return render (request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
        form = PokemonForm(instance=pokemon)
    return render (request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    pokemon.delete()
    return redirect('pokedex:index')


@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers')
        
    else:
        form = TrainerForm()
    return render (request, 'trainer_form.html', {'form': form})


@login_required
def edit_trainer(request, id: int):
    pokemon = Trainer.objects.get(pk=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers')
    else:
        form = TrainerForm(instance=pokemon)
    return render (request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, id: int):
    trainer = Trainer.objects.get(pk=id)
    trainer.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = "login_form.html"