# Marlym Munoz
# 18 feb 2025
# P2LAB1
# Using the radius, which should be given by the user as a float, the program will calculate the diameter, circumference, and area of a circle.

import math

radius = float(input("What is the radius of a circle? "))

diameter = radius * 2

circumference =2 * radius * math.pi

area = math.pi * math.pow(radius,2)

print(f'The diameter of the cricle is {diameter:.1f}\n')
print(f'The circumference of the circle is {circumference:.2f}\n')
print(f'The area of the circle is {area:.3f}')

##print()
##print()
##print(f'Diameter: {diameter:25.1f}\n')
##print(f'Circumference:{circumference:25.2f}\n')
##print(f'Area {area:25.3f}')
