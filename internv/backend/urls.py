from rest_framework import routers
from django.urls import path, include
from . import views


urlpatterns= [
path('getdata/', views.returnobj,name="returnobj"),

]
