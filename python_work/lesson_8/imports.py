# practice 2/2/25
# chapter 8
# importing modules
import math as m # adding module and labeling
radius = 5 # set the radius to 5
area_one = m.sqrt(m.pi*radius) # area of a cir: pi*r^2 *INCORRECT*
area_two = m.pi*(radius**2) # winner!
print(area_one)
print(area_two)