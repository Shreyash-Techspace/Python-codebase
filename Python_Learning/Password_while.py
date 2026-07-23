correct_password = "Python"

while True:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Correct!")
        break
    else:
        print("Incorrect!")
print("Logged in")
