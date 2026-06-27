# if elif else

"""
if condition_1:
    # Executed if condition_1 is True
    statement_block_1
elif condition_2:
    # Executed if condition_1 is False AND condition_2 is True
    statement_block_2
elif condition_3:
    # Executed if prior conditions are False AND condition_3 is True
    statement_block_3
else:
    # Executed if all above conditions evaluate to False
    fallback_statement_block
"""
name = str(input("Enter your name: "))
marks = float(input("Enter your marks: "))

if marks >= 90:
    print(f"{name}, you got Grade: A")
elif 80 <= marks < 90:  # marks >= 80 and marks < 90:
    print(f"{name}, you got Grade: B")
elif 70 <= marks < 80:  # marks >= 70 and marks < 80:
    print(f"{name}, you got Grade: C")
elif 60 <= marks < 70:  # marks >= 60 and marks < 70:
    print(f"{name}, you got Grade: D")
elif 50 <= marks < 60:  # marks >= 50 and marks < 60:
    print(f"{name}, you got Grade: E")
else:
    print(f"{name}, you got Grade: F")
