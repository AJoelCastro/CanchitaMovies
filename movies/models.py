from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.URLField()
    external_id = models.CharField(max_length=100, unique=True)
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title

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

class WatchList(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
    series = models.ManyToManyField(Series)
    created_at = models.DateTimeField(auto_now_add=True)
