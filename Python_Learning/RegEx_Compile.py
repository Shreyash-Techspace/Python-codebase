import re

phones = "Alice-1234567890, Mark-0987654321, Carol- 0987612345"

pattern = r'\d{10}'
pattern_compiled = re.compile(pattern)

print(pattern_compiled, type(pattern_compiled))

match_obj = (re.findall(pattern_compiled, phones))
print(match_obj)

with open("student_details", 'rt') as fh:
    data = fh.read()
print(data, type(data))

phone_matches = re.finditer(pattern_compiled, data)
print(phone_matches)

for matches in phone_matches:
    print(matches)
