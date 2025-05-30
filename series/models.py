from django.db import models
from generos.models import Genero

class Series(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    first_air_date = models.DateField()
    poster_path = models.URLField()
    external_id = models.CharField(max_length=100, unique=True)
    seasons = models.IntegerField(default=1)
    rating = models.FloatField(default=0.0)
    generos = models.ManyToManyField(Genero, related_name="series")
    trailer_url = models.URLField(blank=True, null=True)
    creator = models.CharField(max_length=200, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"
        ordering = ["-first_air_date"]

class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="season_list")
    season_number = models.IntegerField()
    title = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    poster_path = models.URLField(blank=True, null=True)
    air_date = models.DateField(blank=True, null=True)
    episode_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.series.title} - Temporada {self.season_number}"
        
    class Meta:
        unique_together = ['series', 'season_number']
        ordering = ['season_number']

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="episodes")
    episode_number = models.IntegerField()
    title = models.CharField(max_length=200)
    overview = models.TextField(blank=True, null=True)
    air_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField(help_text="Duración en minutos", default=45)
    still_path = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.season.series.title} - S{self.season.season_number}E{self.episode_number} - {self.title}"
        
    class Meta:
        unique_together = ['season', 'episode_number']
        ordering = ['episode_number']
