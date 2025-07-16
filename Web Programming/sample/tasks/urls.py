from django.urls import path
from . import views
app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add')
    # Add more URL patterns for tasks as needed
]