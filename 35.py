# Question 35: Write a program to create a tuple containing different data types and display it.

mixed_tuple = (1, "OpenAI", 3.14, False, (10, 20))

print("Mixed Tuple:", mixed_tuple)
for item in mixed_tuple:
    print(f"Element: {item} -> Type: {type(item)}")
