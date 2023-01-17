from django.shortcuts import render
from django.http import HttpResponse
from .models import Town
# Create your views here.

def index(request):
    towns = Town.objects.all()
    
    return render(request, 'towns.html', {'towns': towns})

def get_town(request, id):
    town = Town.objects.get(id=id)
    
    return render(request, 'town.html', {'town': town})