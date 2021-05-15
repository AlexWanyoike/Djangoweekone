from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.name