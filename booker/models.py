from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=200)
    code=models.CharField(max_length=20)
    author=models.CharField(max_length=200)
    genre=models.CharField(max_length=100)
    rating=models.IntegerField(null=True)
    publisher=models.CharField(max_length=200)
    price=models.FloatField(null=True)
    stock=models.IntegerField(null=True)


class Favorites(models.Model):
    bookCode=models.CharField(max_length=200)
    customerCode=models.CharField(max_length=200)


