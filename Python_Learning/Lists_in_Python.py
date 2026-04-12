# Normal Way
name = "Shreyash"
age = 20
Percent = 90.55

#  List
"""
    - List is a datatype in which we can store collections of data of data
    - It can store any another type of data in a single datatype
"""
student = ["Shreyash", 20, 90.5]
print(type(student))
print(student)

days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
# +ve INDEXING    0     1       2      3       4      5      6
# -ve INDEXING   -7    -6       -5      -4     -3     -2   -1
print(days_of_week[0])
print(days_of_week[5])
print(len(days_of_week))
print(f"Last day of week is {days_of_week[-1]}")

# if we try to use the index which is not a part of it , it will give error
# print(days_of_week[8]) << error part
