"""
Topic: Sets in Python
Description: Demonstrates set creation,
add(), remove(), and unique values.
"""

# Creating a Set

numbers = {1, 2, 2, 3, 3, 4}

print("Original Set:")
print(numbers)

print()

# Add

numbers.add(5)

print("After Add:")
print(numbers)

print()

# Remove

numbers.remove(2)

print("After Remove:")
print(numbers)

print()

# Length

print("Total Items:", len(numbers))

print()

# Membership

print("Is 3 present?", 3 in numbers)
print("Is 10 present?", 10 in numbers)
