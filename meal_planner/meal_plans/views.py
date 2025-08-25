from django.shortcuts import render

def index(request):
    '''The homepage for Meal Planner'''
    return render(request, 'meal_plans/index.html')