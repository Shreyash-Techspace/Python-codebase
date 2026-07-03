scores = [2, 45, 11, 97, 90, 5, 1, 114]

# TOTAL

total = sum(scores)
print(f"The Total is {total}")

total = 0
for score in scores:
    total = total + score
print(f"The Total is {total}")

# HIGHEST SCORE

highest = max(scores)
print(f"The highest score is {highest}")

highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
print(f"The highest score is {highest}")

# LOWEST SCORE

lowest = min(scores)
print(f"The lowest score is {lowest}")

lowest = scores[0]
for score in scores:
    if score < lowest:
        lowest = score
print(f"The lowest score is {lowest}")
