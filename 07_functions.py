"""
Topic: Functions in Python
Description: Demonstrates function definition,
parameters, and return values.
"""

# Simple Function

def greet():
    print("Hello, Python!")

greet()

print()

# Function with Parameter

def welcome(name):
    print("Welcome,", name)

welcome("Lily")

print()

# Function with Multiple Parameters

def add(a, b):
    print("Sum =", a + b)

add(10, 20)

print()

# Function with Return Value

def multiply(a, b):
    return a * b

result = multiply(5, 4)

print("Result =", result)
