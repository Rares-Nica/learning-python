# Dictionaries - like a struct in C++ but more flexible
person = {
    "name": "Rares",
    "age": "19",
    "goals": ["local AI", "ML engineer", "open source contributor"]
}

# Accessing values
print(person["name"])
print(person["goals"][0])

# Adding a new key on the fly - you can't do this with C++ structs
person["university"] = "UTCN"
print(person)

# Looping through a dictionary
print("\n--- dict items ---")
for key, value in person.items():
    print(f"{key}: {value}")    # only this line is indented

# Everything below has zero indentation — outside the loop
def greet(name, age=18):
    return f"Hello {name}, you are {age} years old."

print("\n--- functions ---")
print(greet("Rares", 19))
print(greet("Someone"))

def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

scores = [85, 92, 78, 95, 88]
minimum, maximum, average = get_stats(scores)
print(f"\nMin: {minimum}, Max: {maximum}, Average: {average}")