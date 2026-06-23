# SETS
"""
- sets are non-sequential collection of items
- comma separated elements enclosed within {}
"""
set1 = {10, "Python", 2.5}
print(set1, type(set1))

# Cannot have indexing with sets
# print(set1[0])  >>> TypeError: 'set' object is not subscriptable

# Length of a set
print(len(set1))
# Sets do not allow Duplicate elements
l1 = [1, 2, 3]
print(l1, type(l1))
s1 = {10, 2.5, 10, 30, 45, 45}
print(s1, type(s1))
