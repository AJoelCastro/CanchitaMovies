from django.db import models

class Genero(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    external_id = models.IntegerField(unique=True, blank=True, null=True)
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="Clase CSS para el ícono")
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ['name']
