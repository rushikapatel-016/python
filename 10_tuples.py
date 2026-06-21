"""
Topic: Tuples in Python
Description: Demonstrates tuple creation,
indexing, count(), and index().
"""

# Creating Tuple

students = ("Lily", "Bee", "Rushika")

print("Tuple:")
print(students)

print()

# Indexing

print("First Student:", students[0])
print("Last Student:", students[-1])

print()

# Length

print("Total Students:", len(students))

print()

# Count

numbers = (1, 2, 2, 3, 2)

print("Count of 2:", numbers.count(2))

print()

# Index

fruits = ("Apple", "Mango", "Banana")

print("Index of Mango:", fruits.index("Mango"))
