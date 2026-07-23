import random

# random() -- returns random float values between 0.0 to 1.0
print(random.random())

# randint(a, b) -- returns random integers values between a and b ( both included)
print(random.randint(1, 10))

# choice(sequence) -- returns random elements from the sequence
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(nums))
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# shuffle(sequence) -- returns the elements shuffled in random sequence
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.shuffle(nums2))
print(nums2)
