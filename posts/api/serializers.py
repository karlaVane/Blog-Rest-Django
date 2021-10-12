from rest_framework import serializers
from posts.models import Posts
from user.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model=Posts
        fields = ['id','title','content','slug','miniature','create_at','published','user','category']
        