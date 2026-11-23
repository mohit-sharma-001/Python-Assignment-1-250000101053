# Question 36: Write a program to create a dictionary containing student details such as roll number, name and marks.

student = {
    "roll_number": 101,
    "name": "Alex Smith",
    "marks": 92.5
}

print("Student Details Dictionary:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
