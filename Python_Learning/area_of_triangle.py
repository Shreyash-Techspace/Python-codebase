"""
when all the length of the sides of the triangle is known - a, b, c
semi perimeter(s)=(a+b+c)/2
Area = square root of (s*(s-a)*(s-b)*(s-c))
"""

a=float(input("ENTER FIRST SIDE: "))
b=float(input("ENTER SECOND SIDE: "))
c=float(input("ENTER THIRD SIDE: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("AREA OF THE TRIANGLE IS: ",round(area,2))