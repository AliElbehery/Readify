from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer, ProfileSerializer
from .models import CustomUser, Profile, UserShelf
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def signup(request):
    serializer= UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        user= CustomUser.objects.get(email= request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token= Token.objects.create(user=user)
        profile= Profile.objects.create(user=user)
        return Response({'user':serializer.data, 'token': token.key}, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
