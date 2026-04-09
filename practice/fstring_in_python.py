"""name = "John"
age = 30
language = "Python"
hours = 3
"""
name = str(input("name: "))
age = int(input("age: "))
language = str(input("language: "))
hours = int(input("hours: "))

# TO PRINT >> John is 20 years old. He studies Python 3 hours a day.
print(name, "is", age, "year old. He studies", language, hours, "hours a day.")

# Using f-string
print(f"{name} is {age} year old. He studies {language} {hours} hours a day.")

sem = int(input("sem: "))
sub1 = int(input("sub1: "))
sub2 = int(input("sub2: "))
sub3 = int(input("sub3: "))

print(f"{name} scored {sub1 + sub2 + sub3} marks in Sem {sem} .")
percent = (sub1 + sub2 + sub3) / 3
print(f"{name} got {percent}% in Sem 1.")
