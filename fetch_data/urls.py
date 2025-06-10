"""
URL configuration for fetch_data project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.urls import path, include
from rest_framework import routers 
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from api.views import UserViewSet,  GroupViewSet, CuisineViewSet,RecipeAPIView
from api.serializers import PermissionViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = routers.SimpleRouter()



router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)  
router.register(r'recipe', CuisineViewSet)
router.register(r'permissions', PermissionViewSet)  # ← this is the fix



urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='home'), 
    path('getting_data/', views.do_fetch, name='do_fetch'),
    path('do_show/', include('get_data.urls')), 
    path('api-auth/', include('rest_framework.urls')), 
    path('api/token/', obtain_auth_token, name='api_token_auth'),  # login
    path('', include('api.urls')), 
    #ath('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cuisine/', RecipeAPIView.as_view(),name='cuisine')
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls 
