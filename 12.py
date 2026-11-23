# Question 12: Write a program to calculate the area and circumference of a circle.

import math

radius = 7.0

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("Radius:", radius)
print(f"Area of circle: {area:.2f}")
print(f"Circumference of circle: {circumference:.2f}")
