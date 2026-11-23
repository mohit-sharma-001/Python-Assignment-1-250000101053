# Question 37: Write a program to create a dictionary containing five countries and their capitals.

capitals = {
    "India": "New Delhi",
    "United States": "Washington, D.C.",
    "United Kingdom": "London",
    "Japan": "Tokyo",
    "France": "Paris"
}

print("Country and Capital pairs:")
for country, capital in capitals.items():
    print(f"{country}: {capital}")
