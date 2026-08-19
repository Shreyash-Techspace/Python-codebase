text = input("Enter text to write to the file: ")

file = open("output.txt", "w")
file.write(text + "\n")
file.close()

print("Data successfully written to output.txt.")

text = input("\nEnter additional text to append: ")

file = open("output.txt", "a")
file.write(text + "\n")
file.close()

print("Data successfully appended.")

file = open("output.txt", "r")

print("\nFinal content of output.txt:")
print(file.read())

file.close()
