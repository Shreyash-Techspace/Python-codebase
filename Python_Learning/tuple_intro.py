"""
TUPLE
 - it is a sequence of items as a collection
 - Syntax: (item1,item2, ...)
"""
t1 = ("Python", 10, 1.5, True, [1, 2, 4], (10, 20))
print(t1)
print(len(t1))

# Accessing items in a tuple
print(t1[1])
print(t1[-2])

t2 = 10, 20, 30, 40
print(t2)
print(type(t2))

# type casting

l1 = [1, 2, 3]
print(l1)
print(type(l1))
l2 = tuple(l1)
print(l2, type(l2))
print(l1, type(l1))

fruits = ("apple", "banana", "cherry")
print(fruits, type(fruits))
fruits = list(fruits)
print(fruits, type(fruits))
