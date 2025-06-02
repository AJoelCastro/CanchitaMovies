from django.shortcuts import render, get_object_or_404
from .models import Genero
from movies.models import Movie
from series.models import Series

# Create your views here.
def menu(request):
    generos = Genero.objects.all().order_by('name')
    return render(request, 'generos/menu.html', {'generos': generos})

def genero_detail(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)
    movies = Movie.objects.filter(generos=genero).order_by('-release_date')[:12]
    series = Series.objects.filter(generos=genero).order_by('-first_air_date')[:12]
    
    context = {
        'genero': genero,
        'movies': movies,
        'series': series,
    }
    
    return render(request, 'generos/genero_detail.html', context)