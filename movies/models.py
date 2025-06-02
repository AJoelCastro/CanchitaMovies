from django.db import models
from generos.models import Genero

class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.URLField()
    external_id = models.CharField(max_length=100, unique=True)
    rating = models.FloatField(default=0.0)
    duration = models.IntegerField(help_text="Duración en minutos", default=90)
    generos = models.ManyToManyField(Genero, related_name="movies")
    trailer_url = models.URLField(blank=True, null=True)
    director = models.CharField(max_length=200, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ["-release_date"]

class WatchList(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
    series = models.ManyToManyField('series.Series')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Lista de {self.user.username}"
    
    class Meta:
        verbose_name = "Lista de Reproducción"
        verbose_name_plural = "Listas de Reproducción"
class Series(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    first_air_date = models.DateField()
    poster_path = models.URLField()
    external_id = models.CharField(max_length=100, unique=True)
    seasons = models.IntegerField(default=1)
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title
