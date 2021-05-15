from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100  )

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100   )

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=100   )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE  )

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE  )
    

    image = models.ImageField(upload_to='media/')

    description = models.TextField()

    def __str__(self):
        return self.name

