from django.db import models

class Category (models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) #url de nuestra categoría
    published = models.BooleanField(default=False)

    #para cuando hagamos un desplegable aparezcan los títulos
    def __str__(self):
        return self.title

