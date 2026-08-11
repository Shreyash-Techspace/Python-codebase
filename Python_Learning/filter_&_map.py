seq = [1, 2, 3, 4, 5]
odd = lambda x: True if x % 2 != 0 else False

# filter(Function, Sequence)
filtered_output = filter(odd, seq)
print(filtered_output)
print(f"Filter_Output: {list(filtered_output)}")

# map(Function, Sequence)
mapped_output = map(odd, seq)
print(mapped_output)
print(f"Mapped_Output: {list(mapped_output)}")
