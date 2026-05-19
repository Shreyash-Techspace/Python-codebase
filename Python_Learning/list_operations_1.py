print("Slicing of Lists")
l1 = [9, 3, 0, 7, 6, 0, 9, 4, 9, 8]
#    {0,1,2,3,4,5,6,7,8,9}
print(l1[0:10:1])
print(l1[2:7:2])

print("Concatenation of List")
l2 = [0, 6, 3]
l3 = [4, 9, 2]
print(l2 + l3)

print("Repetition of List")
l4 = [1, 2, 3, 8, 9, 0, ]
print(l4 * 5)

print("append()")
# add items or elements at the end of the list
# syntax : list_name.append(item)
fruit = ["apple", "banana", "cherry"]
print(fruit)
fruit.append("orange")
print(fruit)

print("insert()")
# add items or elements before the specific index or position
# syntax : list_name.insert(index, item)

cars = ["BMW", "Audi", "Mercedes", "Porsche"]
print(cars)
cars.insert(1, "Ferrari")
print(cars)
