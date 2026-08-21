import re

s1 = "Python is a programming language"

# ^ - Caret => match at the start of the string
pat = r"^[a-z]{8}"
match_object = re.search(pat, s1)
print(match_object)

pat = r"^[A-Z][a-z]{4}"
match_object = re.search(pat, s1)
print(match_object)

# $ - dollar => match at end of the string
pat = r"[a-z]{8}$"
match_object = re.search(pat, s1)
print(match_object)

# () + | - group and or =>
emails = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"(com|edu)"
match_object = re.search(pat, emails)
print(match_object)
