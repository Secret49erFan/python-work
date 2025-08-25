'''Define URL patterns for pizzas'''

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    path('', views.home, name='home')
]