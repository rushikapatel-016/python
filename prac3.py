names = ["Lily", "Emma", "John", "Sophia", "Alex"]

try:
    index = int(input("Enter an index number (0-4): "))
    print("Name:", names[index])

except ValueError:
    print("Error: Please enter a valid integer.")

except IndexError:
    print("Error: Index out of range. Please enter a number between 0 and 4.")