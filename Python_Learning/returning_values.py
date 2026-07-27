def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    return add, sub, mul


val_1 = int(input("Enter first number: "))
val_2 = int(input("Enter second number: "))

res1, res2, res3 = arithmetic(val_1, val_2)
print(f"Addition of {val_1} and {val_2} is {res1}")
print(f"Subtraction of {val_1} and {val_2} is {res2}")
print(f"Multiplication of {val_1} and {val_2} is {res3}")
