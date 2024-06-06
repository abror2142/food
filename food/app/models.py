from django.db import models
from django.contrib.auth.models import User


class FoodType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
class Measurement(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    food_type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Ingredient(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=120)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.name
    

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    