# In Python , we can pass function as argument

def add_1(number):
    return number + 1


def square(number):
    return number ** 2


num = int(input("Enter a number: "))
res = square(add_1(num))
print(f"Output is : {res}")
