"""
Topic: Lists in Python
Description: Demonstrates indexing,
append(), remove(), and sort().
"""

# Creating a List

students = ["Lily", "Bee", "Rushika"]

print("Original List:")
print(students)

print()

# Indexing

print("First Student:", students[0])
print("Last Student:", students[-1])

print()

# Append

students.append("Python")

print("After Append:")
print(students)

print()

# Remove

students.remove("Bee")

print("After Remove:")
print(students)

print()

# Sort

students.sort()

print("After Sort:")
print(students)
