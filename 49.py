# Question 49: Write a program to demonstrate the difference between integer and floating-point values.

int_val = 15
float_val = 15.0

print(f"int_val = {int_val}, type = {type(int_val)}")
print(f"float_val = {float_val}, type = {type(float_val)}")

print("int_val / 2 =", int_val / 2)    # Float division
print("int_val // 2 =", int_val // 2)  # Floor division (integer)
print("float_val / 2 =", float_val / 2)
print("float_val // 2 =", float_val // 2)
