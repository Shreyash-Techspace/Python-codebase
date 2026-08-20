# Quantifier = symbol or characters used for describing quantity
import re

message = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10"

pat = r"[a-z]{4}"
match_object = re.search(pat, message)
print(match_object)

pat = r"[A-Z][a-z]{5}"
match_object = re.search(pat, message)
print(match_object)

pat = r"[A-Z][a-z]{2,5}"  # min 2 , max 5
match_object = re.search(pat, message)
print(match_object)

# + matches 1 or more repetitions of the previous pattern
pat = r"[A-Z][a-z]+"
match_object = re.search(pat, message)
print(match_object)

# ? matches 0 or 1 repetitions of the previous pattern
pat = r"[A-Z][a-z]?"
match_object = re.search(pat, message)
print(match_object)

# * matches 0 or more repetitions of the previous pattern
pat = r"[A-Z][a-z]*"
match_object = re.search(pat, message)
print(match_object)
