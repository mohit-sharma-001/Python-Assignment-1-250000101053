# Question 10: Write a program to swap two variables without using a temporary variable.

a = 50
b = 80

print(f"Before swap: a = {a}, b = {b}")

# Pythonic tuple unpacking swap
a, b = b, a

print(f"After swap: a = {a}, b = {b}")
