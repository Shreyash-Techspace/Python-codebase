"""
- not allowed keys are list, set, dict because they are mutable
- allowed keys are int, str, float, bool, tuple because they are immutable
- keys of a dictionary can only be mutable datatype
- values of a dictionary can be any datatype
"""

student1 = {'id': 1001, 'name': 'John', 'marks': [88.5, 71.6, 90.0]}

# accessing inner values
print(student1['marks'][1])

student0 = {'id': 1001, 'name': 'John', 'marks': {'eng': 88.5, 'maths': 71.6, 'sci': 90.0}}
print(student0['marks']['eng'])

# fetching of keys
print(student1.keys(), type(student1.keys()))

# fetching of values
print(student1.values(), type(student1.values()))

# fetching of items
print(student1.items(), type(student1.items()))
