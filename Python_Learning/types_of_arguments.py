def add(a, b):
    return a + b


# Positonal arg : passing te argument in order of their position
result = add(10, 5)
print(result)


# Default arg :
def add(a, b=10):
    print(f"a: {a}, b: {b}")
    return a + b


result1 = add(10, 5)
print(result1)

result1 = add(10)
print(result1)


def add(a, c, b=10):
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c


result2 = add(10, 20, 30)
print(result2)

result2 = add(10, 20)
print(result2)


# The non default arguments should not follow default argument

def add(a, b=10, c=10):
    print(f"a: {a}, b: {b}, c: {c}")
    return a + b + c


# Keyword Argument
result3 = add(10, c=50)
print(result3)

result3 = add(a=10, b=20, c=70)
print(result3)
