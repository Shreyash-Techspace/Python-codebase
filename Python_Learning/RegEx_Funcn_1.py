import re

s1 = "We are learning regex in Python"

# match() => checks match only at the beginning of the string
pat = r"[A-Z][a-z]"
match_obj = re.match(pat, s1)
print(match_obj)

pat = r"[a-z]{3}"
match_obj = re.match(pat, s1)
print(match_obj)

phone = "John-1234567890, Carol-9876545670, Mark-0849549533"
pat = r"[0-9]{10}"
match_obj = re.search(pat, phone)
print(match_obj)

# findall()
phone = "John-1234567890, Carol-9876545670, Mark-0849549533"
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phone)
print(match_obj)

phone = "John-1234567890, Carol-9876545670, Mark-0849549533, Alice-3434340"
pat = r"[0-9]{10}"
match_obj = re.findall(pat, phone)
print(match_obj)

phone = "John-1234567890, Carol-9876545670, Mark-0849549533, Alice-3434340"
pat = r"[0-9]+"
match_obj = re.findall(pat, phone)
print(match_obj)

phone = "John-1234567890, Carol-9876545670, Mark-0849549533, Alice-3434340, Python3.13.5"
pat = r"[0-9]+"
match_obj = re.findall(pat, phone)
print(match_obj)

# fetch all phone no. the phone no. are exactly and should not exceed 15 digit.
pat = r"[0-9]{7,15}"
match_obj = re.findall(pat, phone)
print(match_obj)

# fetch all phone no.s , the no.s are at least 7 digits
pat = r"[0-9]{7,}"  # 7 0r more
match_obj = re.findall(pat, phone)
print(match_obj)

# \b
phone = "John-1234567890, Carol-9876545670, Mark-0849549533, Alice-3434340, Bob-98765432123456789098"
pat = r"[0-9]{7,15}\b"
match_obj = re.findall(pat, phone)
print(match_obj)

phone = "John-1234567890, Carol-9876545670, Mark-0849549533, Alice-3434340, Bob-98765432123456789098"
pat = r"\b[0-9]{7,15}\b"
match_obj = re.findall(pat, phone)
print(match_obj)

# finditer
pat = r"\b[0-9]{7,15}\b"
match_obj_iter = re.finditer(pat, phone)
print(match_obj_iter)
for matches in match_obj_iter:
    print(matches)
