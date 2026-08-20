# Regular Expression (RegEx)
"""
- special sequence of characters that define a patterns for doing complex string matching functionalities
- module => re module (provide a series of metacharacter
"""
import re

message = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10"
'''
# if python is present in message
print("Python" in message)
print("14" in message)
# find the index
print(message.find("Python"))
print(message.find("3.13"))
'''
# Searching in RegEx
"""
re.search(regex_pattern, string) => returns a match object when there is a match found
"""

match_obj = re.search('13', message)
print(match_obj)
print(message[32:34])  # span

if re.search('13', message):
    print("Found a match")
else:
    print("No match")
