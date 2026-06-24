student1 = {"maths": 85.4, "english": 77.5, "phy": 90}

# Fetch the mark of Phy
print(student1["phy"])
# get()
print(student1.get("english"))

# if the key doesnot exist >> Output: None
print(student1.get("chem"))

emp1 = {'id': 1001, 'name': 'Shrey', 'salary': 500000}
print(emp1)
print(emp1.get('phone', 9876543210))  # Default value to the key8
print(emp1.get('id', 9876543210))  # if the key already contain the value, it will not affected by another one

# Membership Operations

print("name" in emp1)
print("call" in emp1)

print("address" not in emp1)

# update
sem1 = {'math': 77, 'eng': 72, 'phy': 73}
sem2 = {'chem': 80, 'bio': 95}

sem1.update(sem2)
print(sem1)

grocery1 = {'milk': 60, 'rice': 100, 'biscuit': 25}
grocery2 = {'rice': 110, 'bread': 15}  # if dict has common keys, then the value will be the latest ones
grocery1.update(grocery2)
print(grocery1)

# pop()
grocery1.pop('rice')
print(grocery1)
grocery1.pop('bread')
print(grocery2)

# keys cannot be duplicated in a dict

shop = {'milk': 60, 'rice': 100, 'bread': 15, 'milk': 60}
