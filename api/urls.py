
from django.urls import path

from api.views import RecipeAPIView 
urlpatterns = [

    path('cuisine/', RecipeAPIView.as_view(), name='recipe-api'),
]