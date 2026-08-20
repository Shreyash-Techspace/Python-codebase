import re

message = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10"
# digits
match_object = re.search("[0-9][0-9]", message)
print(match_object)
match_object = re.search("[0-9][0-9][0-9]", "House number: 251/A")
print(match_object)

# . (Dot) - matches any char except new line (\n)
match_object = re.search("[0-9].[0-9][0-9]", message)
print(match_object)
match_object = re.search("[0-9].[0-9]", message)
print(match_object)
match_object = re.search("[0-9].[0-9]", "House number: 251/A")
print(match_object)

message_1 = "The year is 2011"
match_object = re.search("[0-9].[0-9][0-9]", message_1)  # dot as an any character
print(match_object)

match_object = re.search("[0-9][.][0-9][0-9]", message_1)  # dot as a exact character '.'
print(match_object)
match_object = re.search("[0-9][.][0-9][0-9]", message)
print(match_object)
