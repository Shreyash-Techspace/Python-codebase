# DICTIONARY
"""
- comma separated key-value pais enclosed within {}
- Syntax >> {key1: value1, key2: value2, ......}
- mutable
"""

grocery = {"milk": 60, "biscuit": 55, "rice": 90, "bread": 15}
print((grocery), type(grocery))

# update value of a key, it only changes the value if the key exist in a dict
grocery["milk"] = 65
print(grocery)

# adding keys and value
grocery["eggs"] = 100
print(grocery)
