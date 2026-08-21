# sub() - used to substitute the pattern with another string or substring
import re

s1 = "Sunday, Monday, Tuesday, Monday, Sunday"
pat = "Sunday"
replacement = "Friday"
result = re.sub(pat, replacement, s1)
print(result)

result = re.sub(pat, replacement, s1, count=1)  # replace only the first occurrence
print(result)

s1 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
pat = r"S[a-z]+"  # Anything starting with 'S' will be replaced
replacement = "Friday"
result = re.sub(pat, replacement, s1)
print(result)

message = """We are learning re. Using re we can search for a pattern in a given string.
Using the sub(), we can replace the pattern with a given string as well."""

patt = r're'
replacement = "Regular Expression"
result = re.sub(patt, replacement, message)
print(result)

patt = r'\bre\b'
replacement = "Regular Expression"
result = re.sub(patt, replacement, message, flags=re.IGNORECASE)
print(result)

phone_nums = "+91-1234567890, +91-9999999999"
pattern = r"[+-]"
replacement = ""
result = re.sub(pattern, replacement, phone_nums)
print(result)
