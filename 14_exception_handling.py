try:
    # Get input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform division
    result = num1 / num2

except ValueError:
    print("Error: Please enter only numbers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Division Result:", result)

finally:
    print("Program execution completed.")
