nums = [1, 2, 3, 0, -1]
print(nums)
# Membership operation
print(0 in nums)
print(10 in nums)
print(3 not in nums)
print(5 not in nums)

# Type Casting
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
weekdays = set(weekdays)
print(weekdays, type(weekdays))

# add
set1 = {2, 0, 1}
set1.add(5)
print(set1)

# remove
set2 = {2, 0, 1}
set2.remove(0)
# set2.remove(5) >>> element not present in set will cause error when we use remove()
print(set2)

# discard()
set3 = {2, 0, 1, -1}
set3.discard(0)
print(set3)
set3.discard(10)  # element which not in sets
print(set3)
