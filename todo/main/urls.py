from django.contrib import admin
from django.urls import path,include
from .views import home,remove

urlpatterns = [
    path('',home,name='home' ),
     path('del/<str:item_id>', remove, name="del"),
]