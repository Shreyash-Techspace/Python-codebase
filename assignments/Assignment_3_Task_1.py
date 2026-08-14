# Task 1: Calculate Factorial Using a Function

num = int(input("Enter the Number : "))


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(f"Factorial of {num} is {fact(num)}")
