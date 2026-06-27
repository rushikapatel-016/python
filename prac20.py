try:
    with open("scores.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("scores.txt not found.")

    with open("scores.txt", "w") as file:
        file.write("John: 85\nEmma: 92\nLily: 88\n")

    print("scores.txt has been created successfully.")