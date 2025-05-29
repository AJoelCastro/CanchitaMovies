from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Series
from .services.api_client import ExternalAPIClient

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 12

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

class SeriesListView(ListView):
    model = Series
    template_name = 'movies/series_list.html'
    context_object_name = 'series'
    paginate_by = 12

# Create your views here.
