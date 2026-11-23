# Question 48: Write a program to demonstrate the use of print() with multiple variables and formatted output.

name = "Bob"
age = 21
gpa = 3.85

# Multiple variables with sep and end
print("Name:", name, "Age:", age, "GPA:", gpa, sep=" | ")

# Formatted strings
print(f"Student {name} is {age} years old with GPA {gpa:.2f}")
print("Student {} is {} years old with GPA {:.2f}".format(name, age, gpa))
