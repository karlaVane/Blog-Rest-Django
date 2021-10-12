from django.db import models
from user.models import User
from django.db.models import SET_NULL
from categories.models import Category

class Posts (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255,unique=True)
    miniature = models.ImageField(upload_to='posts/img/')
    create_at = models.DateTimeField(auto_now_add=True) #que se cree de manera automática
    published = models.BooleanField(default=False)
    #Un post es hecho por un usuario y pertenece a una categoría
    user = models.ForeignKey(User, on_delete= SET_NULL, null= True)
    category = models.ForeignKey(Category, on_delete=SET_NULL,null=True)
    
    def __str__(self):
        return self.title


