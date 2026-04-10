s1 = "Python is fun."

# 1. Repetition
# (*): Used to repeat the string or a character

print(s1 * 3)

# 2. Membership Operation (in & not in)
"""
Checks if the string or a character is a part of an another string or not
gives the output in the format of TRUE OR FALSE
"""
# in
print("Python" in s1)
print("i" in s1)
print("z" in s1)

# not in
print("z" not in s1)
print("Java" not in s1)
print("Python" not in s1)

# Comparison of string
print("Python" == "Python")
print("Python" == " Python")

# 3. Strip - strip()
# Removing Spaces from the String

s2 = "       Python     "
s3 = s2.strip()
print(s3)

print(s2.strip() == "Python")

# 4. Replace - replace()
#  -used to replace a part of a string or a character from the string.

s4 = "We are learning Python"
print(s4)
print(s4.replace("Python", "Java"))

# the existing string will not change, it will only replace and give the output
print(s4)
# to store the replaced valued , create new variable
s5 = s4.replace("Python", "Java")
print(s5)

print(s4.replace("e", "E"))
# it will replace all occrence the e's found in the string

# to replace n no. of occurence
print(s4.replace("e", "E", 1))
