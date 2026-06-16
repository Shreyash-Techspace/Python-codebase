fruits = ["apple", "banana", "cherry"]

print("extend")
# add multiple elements at the end of the list
# Syntax: list_name.extend(["a","b","c"])

print(fruits)
fruits.extend(["guava", "pineapple", "mango"])
print(fruits)
print(len(fruits))

print("remove")
# removes the first occurance of element in a list {delete by value}
# Syntax list_name.remove(["a","b","c","a"])
fruits.remove("banana")
print(fruits)

cars = ["audi", "bmw", "toyota", "audi"]
print(cars)
cars.remove("audi")
print(cars)

print("pop")
# Removes the element by given index {delete by position}
# if no indexed is given , it removes last element
# list_name.pop(index position)

print(fruits)
fruits.pop(0)
print(fruits)
fruits.pop()
print(fruits)
