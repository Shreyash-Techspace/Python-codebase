# Module
"""
- any extension of .py is a module
- Built-in modules => math, random, datetime, and many more

Importing a Module in python
- Syntax: import module_name
Importing only few functions/variables
- Syntax: from module_name import f1, f2, f3, .....
Create an alias for the module that is imported
- Syntax: import module_name as alias_name
"""

import math

# Calculate Square root of a number
num = 100
output = math.sqrt(num)  # module.function_name(arg1, arg2, ....)
print(output)

# Calculating the area of a circle
radius = 5
area_of_circle = math.pi * radius ** 2
print(f"Area of circle with radius {radius}: {area_of_circle}")

# Throw a die
from random import randint
value = randint(1, 6)
print(value)

# Aliasing Module
import datetime as dt
time = dt.time(8, 34, 51)
print(time)







