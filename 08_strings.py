"""
Topic: Strings in Python
Description: Demonstrates slicing,
formatting, and string methods.
"""

# String

name = "Python"

print("Original String:", name)

print()

# Slicing

print("First 3 characters:", name[0:3])
print("From index 2:", name[2:])
print("Last character:", name[-1])
print("Reverse string:", name[::-1])

print()

# Formatting

user = "Lily"
age = 19

print(f"My name is {user} and I am {age} years old.")

print()

# String Methods

text = "python programming"

print(text.upper())
print(text.title())
print(text.replace("python", "Java"))
print(text.count("m"))
