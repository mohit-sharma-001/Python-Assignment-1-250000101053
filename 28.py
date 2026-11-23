# Question 28: Write a program to demonstrate the use of abs(), round() and pow() functions.

# abs()
negative_num = -45.67
print(f"abs({negative_num}) =", abs(negative_num))

# round()
float_num = 3.14159265
print(f"round({float_num}, 2) =", round(float_num, 2))
print(f"round({float_num}) =", round(float_num))

# pow()
base = 3
exp = 4
print(f"pow({base}, {exp}) =", pow(base, exp))
print(f"pow(2, 3, 5) [i.e., (2^3) % 5] =", pow(2, 3, 5))
