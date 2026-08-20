import re

s1 = "python is a programming Language. python3.13 is current version"

# [A-Z], [a-z]

pat = r"[A-Z][a-z][a-z]"
match_obj = re.search(pat, s1)
print(match_obj)

# \d and \D
# \d matches 1 digit character. it is similar to [0-9]
pat2 = r"[a -z][a-z][a-z]\d"
match_obj2 = re.search(pat2, s1)
print(match_obj2)

# \D matches 1 non-digit character.
pat2 = r"[a -z][a-z][a-z]\D"
match_obj2 = re.search(pat2, s1)
print(match_obj2)

# \s and \S
# \s matches any whitespace character, tab and newline
pat2 = r"[a -z][a-z][a-z]\s"
match_obj2 = re.search(pat2, s1)
print(match_obj2)

s2 = """Hi there
We are learning Python
"""
print(s2)
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat, s2)
print(match_obj)

# \S matches any character except space, tab , newline
pat = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pat, s2)
print(match_obj)

# \w and \W
# \w matches alphanumeric character such as  [a-z], [A-Z], [0-9],...
pat = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pat, s2)
print(match_obj)

# \W matches a character except [a-z], [A-Z], [0-9]
pat = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pat, s2)
print(match_obj)
