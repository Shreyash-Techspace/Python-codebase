# Opening a files in Python
"""
- open(file_name, mode_to_open)
_ Modes: r(read), x(create), w(write), a(append), t(text file), b(binary file)
- 'rt' is a default mode
"""
file_handler = open("practice.txt", 'rt')
print(file_handler)

# Read Operation

# Closing a file => close()
file_handler.close()
print(file_handler)
