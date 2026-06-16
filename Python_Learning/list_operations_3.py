days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week)

print("reverse")
# reverse the list
# Syntax: listname.reverse()

days_of_week.reverse()
print(days_of_week)

nums = [5, 1, 8, 4, 0, 7, 3]
print(nums)
# used to sort the list in ascending order
# Syntax : list_name.sort()
# for sort in descending order use list_name.sort(reverse=True)

print("sort")
nums.sort()
print(nums)
print("reverse sort")
nums.sort(reverse=True)
print(nums)

print("count")
# count the occurrence of the element
# Syntax: listname.count(element)

numbers = [1, 2, 3, 5, 3, 4, 6, 8, 6, 9, 0, 6, 4, 7]
print(numbers)
c = numbers.count(4)
print(c)

print("Membership Operation")
# in and not in
# tells that the element is present or not in the list , give output in T or F format

language = ["python", "javascript", "c++"]
print(language)
print("python" in language)  # if the element is present in list, it will give T if not it will give F
print("python" not in language)  # if the element is present in list, it will give F if not it will give T
