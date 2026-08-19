# json ( JavaScript Object Notation)
"""
- mainly used in APIs and Data Storage
- widely used format to stores configuration and other things of a file
"""

import json

students = {'student1': {'roll': 101, 'name': 'John', 'percent': 90.3, 'sports': False},
            'student2': {'roll': 102, 'name': 'Carol', 'percent': 91.76, 'sports': False},
            'student3': {'roll': 103, 'name': 'Alice', 'percent': 92.01, 'sports': False}}

print(students, type(students))

# dump() - use for serialization
'''
with open("student_data.json", 'w') as fh:
    json.dump(students, fh, indent=4)
'''

# load() - use for deserialization
'''
with open("student_data.json", 'r') as fh:
    data = json.load(fh)
print(data, type(data))
'''
# update()
# 1. read the old data from the json file
with open("student_data.json", 'r') as fh:
    data = json.load(fh)

# 2. update operation
data.update(students)

# 3. dump - write the updated data
with open("student_data.json", 'w') as fh:
    json.dump(data, fh, indent=4)
