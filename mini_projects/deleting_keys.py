"""
we have the following dictionary containing details:

user = {
    "username": "my_user",
    "password" : "test@124",
    "email" : "user@gmail",
    "address" : "ABC road, 111111",
    "country" : "Australia"
}

delete the sensitive data from the dict present in a list
sensitive_info = { "password", "address" }
"""

user = {
    "username": "my_user",
    "password": "test@124",
    "email": "user@gmail",
    "address": "ABC road, 111111",
    "country": "Australia"
}

sensitive_info = {"password", "address", "phone"}

for i in sensitive_info:
    if i in user:
        print(f"Deleted Key: {i}, and its Value: {user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present")

print(f"The Detail User can see : {user}")
