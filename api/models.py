from django.db import models

class CuisineModel(models.Model):
    id =   models.IntegerField( primary_key = True)
    name = models.CharField(max_length=200,  default="Empty object")
    ingredients = models.CharField(max_length=600,null=True, blank=True, default=None)
    instructions = models.CharField(max_length=600,null=True, blank=True, default=None)
    prepTimeMinutes = models.FloatField(blank=True, default=0, null=True)
    cookTimeMinutes = models.FloatField(blank=True, default=0, null=True)
    servings = models.CharField(max_length=600,null=True, blank=True, default=None)
    difficulty = models.CharField(max_length=600,null=True, blank=True, default=None)
    cuisine = models.CharField(max_length=600,null=True, blank=True, default=None)
    caloriesPerServing = models.CharField(max_length=600,null=True, blank=True, default=None)
    tags = models.CharField(max_length=600,null=True, blank=True, default=None)
    userId = models.CharField(max_length=600,null=True, blank=True, default=None)
    image = models.CharField(max_length=500,null=True, blank=True, default=None)
    rating = models.FloatField( blank=True, default=5.0,null=True)
    reviewCount = models.CharField(max_length=600,null=True, blank=True, default=None)
    mealType = models.CharField(max_length=600,null=True, blank=True, default=None)
    
    def __str__(self):
        return self.name 

