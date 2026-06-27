# FILE HANDLING IN PYTHON
# Modes: r = read, w = write, a = append

# -------------------------
# 1. WRITE MODE (w)
# Creates file or overwrites existing content
# -------------------------

with open("demo.txt", "w") as file:
    file.write("Hello Lily!\n")
    file.write("This is file handling in Python.\n")

print("File written successfully!")

# -------------------------
# 2. APPEND MODE (a)
# Adds new content without deleting old content
# -------------------------

with open("demo.txt", "a") as file:
    file.write("This is an appended line.\n")
    file.write("We are learning Python step by step.\n")

print("Data appended successfully!")

# -------------------------
# 3. READ MODE (r)
# Reads and displays file content
# -------------------------

with open("demo.txt", "r") as file:
    content = file.read()
    print("\n--- FILE CONTENT START ---")
    print(content)
    print("--- FILE CONTENT END ---")
