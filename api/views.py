from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .serializers import GroupSerializer, UserSerializer, CuisineSerializer
from .models import CuisineModel
#from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication as tka


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated] 

class CuisineViewSet(viewsets.ModelViewSet):
    queryset = CuisineModel.objects.all()
    serializer_class = CuisineSerializer 
    permission_classes = [permissions.IsAuthenticated]
    


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from .models import CuisineModel
from .serializers import CuisineSerializer

class RecipeAPIView(APIView):
    authentication_classes = [tka]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        recipes = CuisineModel.objects.all()
        print(recipes)
        serializer = CuisineSerializer(recipes, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        print(request)
        return self.get(request)
        # serializer = CuisineSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
