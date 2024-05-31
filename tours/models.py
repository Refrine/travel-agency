from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    hotel = models.CharField(max_length=155)
    price = models.FloatField()
    image = models.ImageField(upload_to='tours_images/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.title