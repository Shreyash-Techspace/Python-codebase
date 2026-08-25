# Creating a Class

class MyClass:
    pass


# Creating an Object
obj1 = MyClass()
obj2 = MyClass()
# ------ Obj1 and Obj2 are objects of class MyClass

l1 = [10, 20, 40, 30]
print(type(l1))

print(type(obj1))
print(type(obj2))

"""
- Calling methods using Object
    => obj1.method(arg1, arg2, arg3,.........)
    => obj2.method(arg1, arg2, arg3,.........)
"""


class Student:
    """
    This is a class student to manage student information and activities
    """
    pass


s1 = Student()
s2 = Student()

# Doc Strings => __doc__
print(Student.__doc__)

print(help(Student))
