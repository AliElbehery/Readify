from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField()
    image= models.ImageField(upload_to='media/books')
    auther= models.CharField(max_length=50)
    category= models.ForeignKey(Category, on_delete= models.CASCADE)

    def no_of_ratings(self):
        ratings= Rating.objects.filter(book=self)
        return len(ratings)
    
    def avg_rating(self):
        sum=0
        ratings=Rating.objects.filter(book=self)
        if len(ratings) > 0:
            for x in ratings:
                sum +=x.rate
            return sum/len(ratings)
        else:
            return 0
    def __str__(self):
        return self.name
    


class Rating(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    rate= models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    class Meta:
        unique_together= [('user','book'),]
        index_together= [('user','book'),]

    def __str__(self):
        return str(self.id)

class Profile(models.Model):
    user= models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    bio= models.TextField()
    image= models.ImageField(upload_to='media/users')
    shelf= models.ManyToManyField(Book, through='UserShelf')

    def __str__(self):
        return self.user.username


class UserShelf(models.Model):
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    book= models.ForeignKey(Book, on_delete=models.CASCADE)