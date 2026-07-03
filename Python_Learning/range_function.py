# Range()
"""
- range()- built-in function used to generate sequence of integer in a given interval
- 1. (start, stop, step)
- 2. (start, stop) >> step = 1 by default
- Syntax1:
  for i in range(start, stop, step):
    statements
"""
print("1 to 9")
for i in range(1, 10, 1):
    print(i)

print("\nodd")
for j in range(1, 11, 2):
    print(j)

print("\neven")
for k in range(0, 10, 2):
    print(k)

print("\nReverse order from 20 to 10")
for l in range(20, 9, -1):
    print(l)

"""
- Syntax2:
  for i in range(start, stop):
    statements
"""

for s in range(1, 5):
    print(s)

"""
Syntax3:
  for i in range(stop):
    statements
"""
for t in range(10):
    print(t)

grocery = ['salt', 'milk', 'butter']
for index in range(len(grocery)):
    print(grocery[index])
    print(index)

profit = [9, 11, 6, 19]
for index in range(len(profit)):
    q = index + 1
    print(f"Profit for Quater {q} is {profit[index]}")
