# 1. count()
"""
 - counts the number of occurrence of the substring or a character in a main string or a string
 - Syntax - string.count(substring/character)
 - can find the occurrence of any characters
"""
s1 = "We are learning Python. Python is fun."
print(s1.count("Python"))

s2 = "Python"
print(s1.count(s2))
print(f"Occurrences of {s2} is {s1.count(s2)} ")

# NOTE -> we can also calculate the occurrences of space by simply putting s2 = " "

# 2. Cases
"""
 - Changes the case of the string 
 - cases are upper(), lower(), title(), capitalize(), etc
 - syntax - string.case()
"""

s3 = "wE arE LearNiNG PyThOn3.15"

#  A] upper() - changes whole string to uppercase
print(s3.upper())

#  B] lower() - changes whole string tp lowercase
print(s3.lower())

#  C] title() - changes all initial letter of a substring to uppercase in a string
"""
example. s1 = "i am shreyash"
output = I Am Shreyash
"""
print(s3.title())

#  D] capitalize() - changes the first letter of the entire string to uppercase and rather than the first character of a string all initials will be in lowercase
"""
example. s1 = "i am Shreyash"
output = I am shreyash
"""
print(s3.capitalize())

# 3. startswith() AND endswith()
"""
 - checks if the string is starting/ending with a another substring or a character or not
 - gives output in the form of True or False 
"""
s5 = "We are learning Python"

#  A] startswith()
print(s5.startswith("We"))
print(s5.startswith("W"))
print(s5.startswith("w"))
print(s5.startswith("are"))

#  B] endswith()
print(s5.endswith("Python"))
print(s5.endswith("n"))
print(s5.endswith("N"))
print(s5.endswith("Pytho"))

# NOTE -> Python is case-sensitive , its checks for the exact substring
