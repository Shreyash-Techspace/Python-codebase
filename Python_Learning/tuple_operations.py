# CONCATENATION
s1 = ("Nexa", 41)
s2 = (99, 99.5, 80, 90)
print(s1 + s2)

# REPETITION
a1 = ("Bar", 50000)
print(a1 * 3)

# MEMBERSHIP
print(99 in s2)
print("shrey" in s2)
print(99.6 not in s2)
print(80 not in s2)

# COUNT
b1 = (5, 7, 3, 9, 2, 1, 9, 0)
# tuple_name.count(element)
print(b1.count(9))

#  INDEX
# tuple_name.index(element)
print(b1.index(9))
# print(b1.index(39))

# MIN
# min(tuple_name)
print(f"smallest no. is {min(b1)}")

# MAX
# max(tuple_name)
print(f"biggest no. is {max(b1)}")

# SUM
# sum(tuple_name)
print(f"total is {sum(b1)}")
