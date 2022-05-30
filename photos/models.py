from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length =50, null=False, blank=False)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =20, null=False, blank=False)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    image_name = models.CharField(max_length =30)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description