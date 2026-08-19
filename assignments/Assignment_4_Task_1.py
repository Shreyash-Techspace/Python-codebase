try:
    file = open("sample.txt", "r")
    print("Reading from file")

    for line in file:
        print(line, end="")
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist")
