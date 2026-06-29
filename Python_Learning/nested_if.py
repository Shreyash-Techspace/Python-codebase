# Nested if
# Syntax:
"""
if outer_condition_1:
    # Executes if outer_condition_1 is True
    if inner_condition_A:
        # Executes if both outer_condition_1 and inner_condition_A are True
        print("Inner code block A")
    elif inner_condition_B:
        # Executes if outer_condition_1 is True but inner_condition_A is False
        print("Inner code block B")
    else:
        # Executes if outer_condition_1 is True but both inner conditions are False
        print("Inner else block")

else:
    # Executes if all outer conditions are False
    print("Outer else block")
"""

name = str(input("Enter your name: "))
marks = float(input("Enter your Marks: "))

if marks >= 60:
    print(f"{name}, You are Pass.")
    if marks >= 90:
        print("You got Grade: A")
    elif 80 <= marks < 90:  # marks >= 80 and marks < 90:
        print("You got Grade: B")
    elif 70 <= marks < 80:  # marks >= 70 and marks < 80:
        print("You got Grade: C")
    else:
        print("You got Grade: D")
else:
    print(f"{name}, You are Fail.")
