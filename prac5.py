try:
    with open("credentials.txt", "r") as file:
        lines = file.readlines()

    # Check if the file has exactly 2 lines
    if len(lines) != 2:
        print("Error: Invalid file format.")

    else:
        # Remove newline characters
        saved_username = lines[0].strip()
        saved_password = lines[1].strip()

        # Ask user for login details
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Compare credentials
        if username == saved_username and password == saved_password:
            print("Login Successful!")

        else:
            print("Invalid username or password.")

except FileNotFoundError:
    print("Error: credentials.txt file not found.")