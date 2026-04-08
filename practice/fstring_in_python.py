name = "John"
age = 30
language = "Python"
hours = 3

# TO PRINT >> John is 20 years old. He studies Python 3 hours a day.
print(name, "is", age, "year old. He studies", language, hours, "hours a day.")

# Using f-string
print(f"{name} is {age} year old. He studies {language} {hours} hours a day.")

sub1 = 78
sub2 = 87
sub3 = 91
print(f"{name} scored {sub1 + sub2 + sub3} marks in Sem 1.")
percent = (sub1 + sub2 + sub3) / 3
print(f"{name} got {percent}% in Sem 1.")
