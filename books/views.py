from django.shortcuts import render
from books.models import Book, Profile, UserShelf, Rating, Category
from rest_framework import viewsets
from books.serializers import BookSerializer, ProfileSerializer, RatingSerializer, UserShelfSerializer, CategorySerializer
# Create your views here.



class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    serializer_class= BookSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset= Profile.objects.all()
    serializer_class= ProfileSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset= Rating.objects.all()
    serializer_class= RatingSerializer

class UserShelfViewSet(viewsets.ModelViewSet):
    queryset= UserShelf.objects.all()
    serializer_class= UserShelfSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class= CategorySerializer