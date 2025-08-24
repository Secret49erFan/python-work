from django.db import models

class Pizza(models.Model):
    '''A type of pizza.'''
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
class Topping(models.Model):
    '''Types of toppings for pizza.'''
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)