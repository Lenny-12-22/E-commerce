from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image= models.ImageField()
    category=models.ForeignKey(Category, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name