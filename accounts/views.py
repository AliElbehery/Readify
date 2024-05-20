from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, viewsets
from books.models import Profile

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


@api_view(['POST'])
def login(request):
    user= get_object_or_404(CustomUser, email= request.data['email'])
    if not user.check_password(request.data['password']):
        return Response('Incorrect Password', status=status.HTTP_400_BAD_REQUEST)
    token, created= Token.objects.get_or_create(user=user)
    profile, created= Profile.objects.get_or_create(user=user)
    serializer= UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data}, status= status.HTTP_202_ACCEPTED)


class UserList(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class= UserSerializer

