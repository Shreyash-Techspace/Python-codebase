import re

with open("students_details2", "rt") as fh:
    data = fh.read()

pattern = r"\b[a-zA-Z][\w.-]+[@][a-z]+[.][a-z]+\b"
match_obj = re.finditer(pattern, data)

for matches in match_obj:
    print(matches)
