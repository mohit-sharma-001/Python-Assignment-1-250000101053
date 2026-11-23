# Question 27: Write a program to demonstrate the use of int(), float() and str() functions.

val_str = "150"
val_float_str = "45.75"
val_num = 100

# Using int()
res_int = int(val_str)
print("int('150') ->", res_int, type(res_int))

# Using float()
res_float = float(val_float_str)
print("float('45.75') ->", res_float, type(res_float))

# Using str()
res_str = str(val_num)
print("str(100) ->", res_str, type(res_str))
