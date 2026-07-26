# Task 1: Check if a Number is Even or Odd
"""
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""
print("Even Odd Check")
num = int(input("Enter your number: "))

if num % 2 == 0:
    print(f"The number {num} is an even")
else:
    print(f"The number {num} is an odd")
