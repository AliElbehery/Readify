from rest_framework import serializers
from .models import Profile, Book,UserShelf,Rating, Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields= ['name','description','auther', 'category', 'image','no_of_ratings','avg_rating']


class UserShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserShelf
        fields= '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rating
        fields= '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields= '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'