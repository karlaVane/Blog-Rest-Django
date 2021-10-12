from django.db import models
from user.models import User
from django.db.models import CASCADE #Cuando se borre un usuario tambien se borra sus comentarios
from posts.models import Posts

class Comment (models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= CASCADE,null=True)
    post = models.ForeignKey(Posts, on_delete=CASCADE,null=True)
    