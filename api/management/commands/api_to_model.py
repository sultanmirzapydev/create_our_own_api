import csv
from django.http import HttpResponse
from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import render
import requests as re
from ...models import CuisineModel

def get_data():
    url = 'https://dummyjson.com/recipes'
    response = re.get(url)
    recipes = response.json()['recipes'] 
    for recipe in recipes:
       # recipe.pop('id')
        print(recipe)
       
        CuisineModel(**recipe).save()

    


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_data()











