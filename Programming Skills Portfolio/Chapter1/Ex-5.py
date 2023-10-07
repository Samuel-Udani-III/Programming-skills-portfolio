"""
Chapter 1
Exercise 5
Write a Python program which accepts the radius of a circle from the user and compute the area.

     
"""
#Import pi from the python database and use float to calculate the radius
from math import pi
r= float(input("radius="))
print("area=",(pi*r**2))