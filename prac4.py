def safe_divide(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

    except TypeError:
        print("Error: Invalid data type.")
        return None


# Function Calls
print(safe_divide(20, 4))
print(safe_divide(20, 0))
print(safe_divide("hello", 5))