from django.shortcuts import render

def home(request):
    '''The home page for Pizzeria Project'''
    return render(render, 'pizzas/home.htm')