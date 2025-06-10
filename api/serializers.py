from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import CuisineModel 
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import Permission
from rest_framework import permissions
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.permissions import IsAuthenticated

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #fields = ['url', 'username', 'email', 'groups','password','date_joined']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group 
        #fields = '__all__'
        fields = ['url', 'name',]

class CuisineSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = CuisineModel

        fields = '__all__'

class PermissionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ['url', 'id', 'name', 'codename', 'content_type']

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAdminUser]  # or customize



     