from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Animal(models.Model):
    # including to demonstrate Class Based Api Views..
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Animal Name: {self.name}"

class Movie(models.Model):
    # including to demonstrate ModelMixins and usaged of Generic Views.
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return f"Movie Name: {self.name}"
