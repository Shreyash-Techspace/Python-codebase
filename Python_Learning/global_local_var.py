n = 1  # GLOBAL VARIABLE


def fn():
    n = 5  # LOCAL VARIABLE
    print(f"in {n} ")


fn()

print(f"out {n}")
