# Question 33: Write a program to create a list containing different data types.

mixed_list = [101, "Python", 98.6, True, [1, 2, 3]]

print("Mixed Data Type List:", mixed_list)
for item in mixed_list:
    print(f"Item: {item} -> Type: {type(item)}")
