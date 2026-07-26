countries = ["India", "United States", "Australia", "Ireland", "Sri Lanka", "Iceland", "Cuba", "Iran"]

# Count all the countries which are starting with "I" and list them all

counter = 0
output = []
for country in countries:
    if country[0] == "N":
        counter += 1
        output.append(country)

print(f"Found {counter} countries")
print(output)
