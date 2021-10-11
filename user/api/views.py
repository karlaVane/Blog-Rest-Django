import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user.models import User
from user.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated

class registerView(APIView):
    def post (self, request):
        serializerP = UserRegisterSerializer(data = request.data)
        if serializerP.is_valid(raise_exception=True):
            serializerP.save()
            return Response(serializerP.data)

        return Response(serializerP.errors, status= status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated] #Solo los usuarios autenticados podrán ver sus datos

    def get(self, request):
        serializerG = UserSerializer(request.user)
        return Response(serializerG.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializerP = UserUpdateSerializer(user , request.data)
        if serializerP.is_valid(raise_exception=True):
            serializerP.save()
            return Response(serializerP.data)

        return Response(serializerP.errors,status=status.HTTP_400_BAD_REQUEST)
