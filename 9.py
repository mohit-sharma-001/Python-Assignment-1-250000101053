# Question 9: Write a program to swap two variables using a temporary variable.

x = 15
y = 30

print(f"Before swap: x = {x}, y = {y}")

temp = x
x = y
y = temp

print(f"After swap: x = {x}, y = {y}")
