"""
- Compile time error = > Syntax error and Indentation error
- Exceptions => Errors during execution
"""

# How to Handle Exception => try-except block

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("The Denominator is Zero")
except ValueError:
    print("Input is not a number")
