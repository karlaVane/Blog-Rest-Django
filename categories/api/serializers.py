from django.db import models
from django.db.models import fields
from rest_framework import serializers
from categories.models import Category

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','slug','published']