"""
Topic: Dictionaries in Python
Description: Demonstrates key-value pairs,
adding, updating, removing, and accessing data.
"""

# Creating Dictionary

student = {
    "name": "Lily",
    "age": 19,
    "city": "Bharuch"
}

print("Original Dictionary:")
print(student)

print()

# Accessing Values

print("Name:", student["name"])
print("Age:", student["age"])

print()

# Adding Data

student["course"] = "Python"

print("After Adding:")
print(student)

print()

# Updating Data

student["age"] = 20

print("After Updating:")
print(student)

print()

# Removing Data

student.pop("city")

print("After Removing:")
print(student)

print()

# Keys and Values

print("Keys:", student.keys())
print("Values:", student.values())

# items

print(student.items())
