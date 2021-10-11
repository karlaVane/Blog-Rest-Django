from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from user.models import User

class UserRegisterSerializer (ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','password'] #El id se autogenera
    
    #Para encriptar la contraseña
    def create(self,validated_data):
        password = validated_data.pop('password', None) #
        instance = self.Meta.model(**validated_data) #
        if password is not None:
            instance.set_password(password)#contraseña encriptada
        instance.save()
        return instance

class UserSerializer (ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
