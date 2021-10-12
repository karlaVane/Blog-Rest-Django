from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from comments.models import Comment
from user.api.serializers import UserSerializer

class CommentSerializer (ModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = Comment
        fields = ['id','content','created_at','user','post']