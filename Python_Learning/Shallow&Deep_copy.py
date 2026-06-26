import copy

l1 = [1, 2.5, [10, 20, 30], "Python"]
print(f"Original list: {l1}")
print("Shallow Copy")
# Shallow copy - the change in element of one mutable datatype will not affect the another same mutable datatype except if it will internal element
l2 = copy.copy(l1)

l1[0] = 5
l1[2][1] = 15
print(f"l1: {l1}")
print(f"l2: {l2}")

print("Deep copy")
# Deep copy - the change in element of one mutable datatype will affect the another same mutable datatype
l2 = copy.deepcopy(l1)

l1[0] = 5
l1[2][1] = 15
print(f"l1: {l1}")
print(f"l2: {l2}")
