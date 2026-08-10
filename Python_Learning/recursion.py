"""
Recursion is a process in which a function calls itself till a certain condition is not true
Factorial of n => n * (n-1) * (n-2) * ........ 2 * 1
n!
Ex: 4! = 4*3*2*1 = 24

n! = n * (n-1) * (n-2) * ........ 2 * 1
   = n * (n-1)!
   = n * (n-1) * (n-2)! ....

There are 2 Parts to any recursive function
1. Base/Terminal Condition
2. Recursive Condition

"""


# Without Recursion
def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


n1 = int(input("Enter a number (without Recursion) : "))
print(f"Factorial of {n1} is {fact(n1)}")


# With Recursion
def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact_rec(num - 1)
        return factorial


n2 = int(input("Enter a number (with Recursion) : "))
print(f"Factorial of {n2} is {fact_rec(n2)}")

# LOGIC
"""
    {24}
fact_rec(4)
           {6}
    4 * fact_rec(3)
                    {2}
            3 * fact_rec(2)
                          {1}
                    2 * fact_rec(1) 
                      
                            1
                            
"""
