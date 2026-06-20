"""
Topic: Loops in Python
Description: Demonstrates for loops and while loops.
"""

# For Loop Example

print("For Loop Example")

for i in range(1, 6):
    print(i)

print()

# For Loop with Step

print("Even Numbers from 2 to 10")

for i in range(2, 11, 2):
    print(i)

print()

# While Loop Example

print("While Loop Example")

count = 1

while count <= 5:
    print(count)
    count += 1

print()

# Multiplication Table Example

number = 5

print("Multiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
