"""
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.

"""
fname=str(input("Enter your first name: "))
lname=str(input("Enter your last name: "))
flname=fname+" "+lname
print(f"Hello, {flname}! Welcome to Python Programming.")
