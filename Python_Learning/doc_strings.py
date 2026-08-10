def func():
    """
    This is a docstring
    We can write what the functon does here
    :return: None
    """
    return None


func()


def divide(num1, num2):
    """
    num1: A number to be divided (Numerator)
    num2: A number that divides num1 (Denominator)
    :return:  float (if num2 is non-zero) or str (if num2 is zero)
    """
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        result = num1 / num2
        return result


print(divide(2, 3))
help(divide)
help(len)
