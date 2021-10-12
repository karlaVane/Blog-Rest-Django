from django.contrib import admin
from posts.models import Posts

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','user','category','create_at','published']