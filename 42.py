# Question 42: Write a program to demonstrate the use of the id() function for different variables.

x = 10
y = 10
z = 25

print(f"Value of x = {x}, id(x) = {id(x)}")
print(f"Value of y = {y}, id(y) = {id(y)}")
print(f"Value of z = {z}, id(z) = {id(z)}")
print("Does x and y point to the same memory object?", id(x) == id(y))
