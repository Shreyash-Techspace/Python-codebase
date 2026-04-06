"""
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# addition
Add = num1 + num2
print("Addition is: ", Add)
# subtraction
Sub = num1 - num2
print("Subtraction is: ", Sub)
Mul = num1 * num2
print("Multiplication is: ", Mul)
Div = num1 / num2
print("Division is: ", Div)
