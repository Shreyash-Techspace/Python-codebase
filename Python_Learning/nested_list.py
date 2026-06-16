print("Nested List")
# List/s inside a list
l1 = [5, 1.5, "Hello", 3.14, [1, 2, 4], 10]
print(l1)
print(len(l1))
print(l1[4])
print(l1[4][0])

l2 = [[1, 2], [3, 4], [5, 6, [0, 9]]]
print(l2)
print(l2[-1])
print(l2[-1][-1])
print(l2[-1][-1][0])
print(l2[-1][-1][1])
