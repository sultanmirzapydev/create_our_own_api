from django.urls import path
from . import views

urlpatterns = [
    path('', views.do_show, name='do_show'),
]