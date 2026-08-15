file_handler = open("practice.txt", 'rt')
print(file_handler)

# Read Operation
'''
read() => reads the content of the file as string
content = file_handler.read()
'''

# readline()
"""
line1 = file_handler.readline()
line2 = file_handler.readline()
line3 = file_handler.readline()
line4 = file_handler.readline()
# want to run certain character of the file => file_name.read(number)
"""

# readlines()
lines = file_handler.readlines()

# Closing a file => close()
file_handler.close()

# print(content, type(content))
'''
print(f"Line1: {line1}")
print(f"Line2: {line2}")
print(f"Line3: {line3}")
print(f"Line4: {line4}")
'''

print(f"Lines: {lines}", type(lines))
