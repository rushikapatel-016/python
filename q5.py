import os

try:
    files = os.listdir()

    txt_files = []

    for file in files:
        if file.endswith(".txt"):
            txt_files.append(file)

    if len(txt_files) == 0:
        raise FileNotFoundError("No .txt files found.")

    print("Text files in the current directory:")

    for file in txt_files:
        print(file)

    print("Total .txt files:", len(txt_files))

except FileNotFoundError as e:
    print(e)