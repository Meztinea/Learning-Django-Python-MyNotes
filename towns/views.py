from django.shortcuts import render
from django.http import HttpResponse
from .models import Town
# Create your views here.

def index(request):
    towns = Town.objects.all()
    
    return render(request, 'towns.html', {'towns': towns})
