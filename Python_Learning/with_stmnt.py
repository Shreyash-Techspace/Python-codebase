# with statement
"""
- do not need to call .close() explicitly.
- we can create a new fie
- SYNTAX : with open("example.txt", mode) as file:
"""

with open("practice.txt", 'rt') as fh:
    contents = fh.read()

print(contents)
