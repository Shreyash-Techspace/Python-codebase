# raise => custom raised error

age = int(input("Enter your age: "))

if age < 0:
    raise Exception("Your age cannot be negative")
#   raise Exception("Your age cannot be negative")
else:
    if age >= 18:
        print("You are old enough to vote")
    else:
        print("You are not old enough to vote")
