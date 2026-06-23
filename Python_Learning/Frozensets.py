# Sets are Mutable
s1 = {1, 2, 4, 8}
print(s1, type(s1))
s1.add(16)
print(s1)
s1.remove(16)
print(s1)

# Frozen Sets - Immutable sets
fs1 = frozenset([1, 2, 3, 4, 5])
print(fs1, type(fs1))

"""
fs1.add(40)
print(fs1) >>> AttributeError: 'frozenset' object has no attribute 'add'
"""

# we cannot do operations like add, remove etc on frozen sets but we can perform operation like union, intersection , etc
fs2 = frozenset({100, 20, 30, 45, 55})
print(fs2, type(fs2))
fs3 = frozenset({10, 20, 30, 40, 50})
print(fs3, type(fs3))

print(fs2 & fs3)  # intersection
print(fs2 | fs3)  # union
print(fs2 - fs3)  # differences
