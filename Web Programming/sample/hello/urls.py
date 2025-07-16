from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('greet/<str:name>/', views.greet, name='greet'),
    path('template/', views.indexUsingTemplate, name='index_using_template'),
    path('template/greet/<str:name>/', views.greetUsingTemplate, name='greet_using_template'),
    # Add more URL patterns as needed
]